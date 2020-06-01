from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.create,name = 'create'),
    re_path(r'(?P<pk>[0-9]+)/upvote', views.upvote,name = 'upvote'),
    re_path(r'(?P<pk>[0-9]+)/downvote', views.downvote,name = 'downvote'),

]
