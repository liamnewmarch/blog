from django.urls import path

from . import views

urlpatterns = (
    path('', views.blog_post_list, name='blog-post-list'),
    path('<slug:slug>/', views.blog_post_detail, name='blog-post-detail'),
)
