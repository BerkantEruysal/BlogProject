from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Blog(models.Model):
    header = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now_add= True)
    content_text = models.TextField()
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)



