from django.urls import path

from blogs.views import IndexView, BlogDetailView, SignUpView, CreateBlogView, EditBlogView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('create-blog/', CreateBlogView.as_view(), name='create_blog'),
    path('<int:pk>/edit', EditBlogView.as_view(), name='edit_blog')
]