from django.urls import path

from blogs.views import IndexView, BlogDetailView, SignUpView, CreateBlogView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blogDetail'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('createBlog/', CreateBlogView.as_view(), name='createBlog')

]