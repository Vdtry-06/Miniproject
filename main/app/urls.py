from django.urls import path
from django.views.generic import RedirectView
from .api_views import get_user, create_user, user_detail
from .api_views import get_video, create_video, video_detail
from .api_views import create_user_feedback, get_user_feedback, user_feedback_detail 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:video_id>/', views.home, name='home'),
    path('<int:video_id>/next/', views.next_video, name='next_video'),
    path('<int:video_id>/previous/', views.previous_video, name='previous_video'),
    # path('save_interaction/<int:video_id>/', views.save_user_interaction, name='save_user_interaction'),
    path('users/', get_user, name = 'get_user'),
    path('users/create', create_user, name = 'create_user'),
    path('users/<int:pk>', user_detail, name = 'user_detail'),
    path('videos/', get_video, name = 'get_video'),
    path('videos/create', create_video, name = 'create_video'),
    path('videos/<int:pk>', video_detail, name = 'video_detail'),
    path('users_feedback/', get_user_feedback, name = 'get_user_feedback'),
    path('users_feedback/create', create_user_feedback, name = 'create_user_feedback'),
    path('users_feedback/<int:pk>', user_feedback_detail, name = 'user_feedback_detail'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]
