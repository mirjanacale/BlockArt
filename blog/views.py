from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView

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
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_on')

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
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author

# About Page


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Like Post View


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        print(f"User {request.user} unliked post {post.id}")
    else:
        post.likes.add(request.user)
        print(f"User {request.user} liked post {post.id}")
        print(f"Total likes: {post.likes.count()}")
    return redirect('post-detail', pk=pk)

# Search View
def test_func(self):
    obj = self.get_object()
    if self.request.user != obj.author:
        print(f"[SECURITY] User {self.request.user} tried to delete post {obj.id} by {obj.author}")
    return self.request.user == obj.author
