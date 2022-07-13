from django.contrib import admin
from .models import Blog, Comment, BlogLike
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogLike)
