from django.views.generic import ListView, DetailView
from blogs.models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class IndexView(ListView):
    model = Blog
    template_name = "blogs/index.html"
    context_object_name = 'blog_list'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'

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
    template_name = 'blogs/create_blog.html'
    fields = ['header', 'content_text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditBlogView(LoginRequiredMixin, UpdateView ):
    model = Blog
    fields = ['header', 'content_text']
    template_name = "blogs/edit_blog.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("blog_detail", kwargs={'pk': self.object.pk})

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            raise PermissionDenied
        return super(EditBlogView, self).dispatch(request, *args, **kwargs)



