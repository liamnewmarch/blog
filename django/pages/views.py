from django.shortcuts import render

from blog.models import Post
from projects.models import Project

from .models import Home


def home_page(request):
    page, _ = Home.objects.get_or_create()
    projects = Project.objects.all()

    if request.user.is_authenticated:
        blog_posts = Post.objects.filter(visibility__in=(
            Post.Visibility.DRAFT,
            Post.Visibility.PUBLISHED,
        ))
    else:
        blog_posts = Post.objects.filter(visibility=Post.Visibility.PUBLISHED)

    return render(request, 'home-page.html', {
        'page': page,
        'projects': projects,
        'blog_posts': blog_posts,
    })
