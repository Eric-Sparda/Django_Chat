from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):

    user_name = models.CharField('Username', max_length=50)
    user_password = models.CharField('Password', max_length=16)

    def __str__(self):
        return self.user_name
    
class ChatMessage(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.message