from django.shortcuts import render

post = [
    {
        'author': 'Mirjana Cale',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 28, 2024'
    },
    {
        'author': 'Monika Nusi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 29, 2024'
    }
]


# Create your views here.
def home(request):
    context={
        'posts': post
    }
    return render(request, 'blog/home.html', context)  

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
