from django.urls import path
from .views import post_list, post_detail, post_create

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/new/', post_create, name='post_create'),  # Place 'new' BEFORE the slug pattern
    path('post/<slug:slug>/', post_detail, name='post_detail'),
]
