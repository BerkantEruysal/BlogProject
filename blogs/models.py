from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    header = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now_add= True)
    content_text = RichTextField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.header

class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text[:20] + "..."

class BlogLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + "  --  "  + self.blog.header[:20] + "..."


class CommentLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)


        

