from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm  

# Home View - Shows only published posts
def home(request):
    return render(request, 'blog/home.html',
                  {'posts': Post.objects.filter(
                      status='published').order_by('-created_on')})

# Post List View
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(status='published')

# Post Detail View
class PostDetailView(DetailView):
    model = Post

# Create Post View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update Post View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author  

# Delete Post View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  

    def test_func(self):
        return self.request.user == self.get_object().author  

# About Page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
