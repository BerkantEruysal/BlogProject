from django.views.generic import ListView, DetailView
from blogs.models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    model = Blog
    template_name = "blogs/index.html"
    context_object_name = 'blog_list'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blogDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().filter(blog=context['object'])
        return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('index')
    template_name = 'blogs/createBlog.html'
    fields = ['header', 'content_text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
