from django.urls import path

from blogs.views import index

urlpatterns = [
    path('', index )
]