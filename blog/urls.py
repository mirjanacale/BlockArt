from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like_post,
)
from . import views

urlpatterns = [
    path('',
         PostListView.as_view(),
         name='blog-home'),
    path('post/<int:pk>/',
         PostDetailView.as_view(),
         name='post-detail'),
    path('post/new/',
         PostCreateView.as_view(),
         name='post-create'),
    path(
        'post/<int:pk>/update/',
        PostUpdateView.as_view(),
        name='post-update'
    ),
    path(
        'post/<int:pk>/delete/',
        PostDeleteView.as_view(),
        name='post-delete'
    ),
    path(
        'post/<int:pk>/like/',
        like_post,
        name='like-post'
    ),
    path(
        'about/',
        views.about,
        name='blog-about'
    ),
]
