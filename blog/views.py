from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post




# Create your views here.
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
    
def get_queryset(self):
    return Post.objects.filter(status='published').order_by('-created_on')   
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView( LoginRequiredMixin,CreateView):
    model = Post 
    fields = ['title', 'content', ] 
    
class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content'] 
       
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status ='draft'
        return super().form_valid(form)  
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False     
    
    
        
    
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
