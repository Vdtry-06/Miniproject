from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import *
import json
# Create your views here.
def home(request, video_id = None):
    videos = Video.objects.all()
    if video_id:
        video = get_object_or_404(Video, id = video_id)
    else:
        video = videos.first()
    context = {
        'videos': videos,
        'current_video': video,
    }
    return render(request, 'app/home.html', context)

def register(request):
    form = Customer()
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = Customer()
    context = {
        'form': form,
    }
    return render(request, 'app/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, 'user or password not correct!')
    context = {}
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def next_video(request, video_id):
    if request.user.is_authenticated:
        videos = Video.objects.all()
        current_video = get_object_or_404(Video, id = video_id)
        user_status, created = UserStatus.objects.get_or_create(user = request.user, video = current_video)
        if request.method == 'POST':
            feedback_text = request.POST.get('feedback')
            
            # current_video = get_object_or_404(Video, id = video_id)
            if feedback_text:
                user_status.feedback_text = feedback_text
                user_status.save()
                next_video = videos.filter(id__gt = current_video.id).first() or videos.first()
                return redirect('home', video_id = next_video.id)
            
            else:
                context = {
                    'videos': videos,
                    'current_video': current_video,
                    'error': "Please provide feedback before moving to the next video."
                }
                return render(request, 'home.html', context)
        return render(request, 'home.html', {'current_video': current_video})
    else:
        return redirect('login')

def previous_video(request, video_id):
    if request.user.is_authenticated:
        videos = Video.objects.all()
        current_video = get_object_or_404(Video, id = video_id)
        previous_video = videos.filter(id__lt = current_video.id).last() or videos.last()
        previous_status, created = UserStatus.objects.get_or_create(user = request.user, video = previous_video)
        context = {
            'current_video': previous_video,
            'user_status': previous_status,
            'videos': videos
        }
        return render(request, 'app/home.html', context)
    else:
        return redirect('login')

# @login_required
# def save_user_interaction(request, video_id):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, id = video_id)
        user_status, created = UserStatus.objects.get_or_create(user = request.user, video = video)
        if request.method == 'POST':
            action = request.POST.get('action')
            user_status.likes = False
            user_status.tym = False
            user_status.dislike = False
            
            if action == 'like':
                user_status.likes = not user_status.likes
            elif action == 'tym':
                user_status.tym = not user_status.tym
            elif action == 'dislike':
                user_status.dislike = not user_status.dislike
            elif action == 'feedback':
                feedback_text = request.POST.get('feedback')
                user_status.feedback_text = feedback_text
                
            user_status.save()
            return redirect('home', video_id = video.id)
        return render(request, 'home.html', {'video': video})
    else:
        return render(request, 'home.html')
