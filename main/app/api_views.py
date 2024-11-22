from .models import Video, UserStatus
from .serializers import UserSerializer, VideoSerializer, UserStatusSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)
    
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_video(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many = True)
    return Response(serializer.data)
    
@api_view(['POST'])
def create_video(request):
    serializer = VideoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def video_detail(request, pk):
    try:
        video = Video.objects.get(pk = pk)
    except Video.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(video)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = VideoSerializer(video, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_user_feedback(request):
    users_feedback = UserStatus.objects.all()
    serializer = UserStatusSerializer(users_feedback, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user_feedback(request):
    serializer = UserStatusSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_feedback_detail(request, pk):
    try:
        user_feedback = UserStatus.objects.get(pk = pk)
        
    except UserStatus.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserStatusSerializer(user_feedback)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserStatusSerializer(user_feedback)
        return Response
    if request.method == 'PUT':
        serializer = UserSerializer(user_feedback, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        user_feedback.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)