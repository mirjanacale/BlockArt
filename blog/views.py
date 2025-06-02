from django.shortcuts import render, get_object_or_404, redirect
from users.forms import CommentForm
from users.models import Comment
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm




# --- Homepage View ---
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-created_on"]
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(status="published").order_by("-created_on")


# --- Posts by a Specific User ---
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user, status="published").order_by(
            "-created_on"
        )


# --- Post Detail ---

class PostDetailView(DetailView):
    model = Post
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = self.object
                comment.user = request.user
                comment.save()
                messages.success(request, "Your comment was added!")
                return redirect('post-detail', pk=self.object.pk)
            else:
                messages.error(request, "There was a problem with your comment.")
        return self.get(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.order_by('-created_on')
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        return context


# --- Create a New Post ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog-home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your post has been created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form validation failed:", form.errors)
        return super().form_invalid(form)


# --- Update a Post ---
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your post has been updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form validation failed:", form.errors)
        return super().form_invalid(form)

    def test_func(self):
        return self.request.user == self.get_object().author


# --- Delete a Post ---
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog-home")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your post was deleted.")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user == self.get_object().author


# --- About Page ---
def about(request):
    return render(request, "blog/about.html", {"title": "About"})


# --- Like/Unlike a Post ---
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.info(request, "You unliked this post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "You liked this post!")
    return redirect("post-detail", pk=pk)


# --- Custom Error Views ---
def custom_404(request, exception):
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    return render(request, "errors/500.html", status=500)


def custom_403(request, exception):
    return render(request, "errors/403.html", status=403)


def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Save the email to your model or mailing list here
        # You can add a success message or redirect as needed
        return HttpResponseRedirect('/')  # or wherever you want
    return HttpResponseRedirect('/')
