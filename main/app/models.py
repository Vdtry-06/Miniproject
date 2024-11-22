from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

# Create your models here.
class Customer(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class Video(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    video_file = models.FileField(upload_to = 'videos/')
    
    def __str__(self):
        return self.title

class UserStatus(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    video = models.ForeignKey(Video, on_delete = models.CASCADE)
    likes = models.BooleanField(default = False)
    tym = models.BooleanField(default = False)
    dislike = models.BooleanField(default = False)
    feedback_text = models.TextField()
    
    def __str__(self):
        return f'Feedback from {self.user.username} on video "{self.video.title}"'