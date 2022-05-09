from django.shortcuts import get_object_or_404, render

from .models import Post


def blog_post_list(request):
    if request.user.is_authenticated:
        blog_posts = Post.objects.filter(visibility__in=(
            Post.Visibility.DRAFT,
            Post.Visibility.PUBLISHED,
        ))
    else:
        blog_posts = Post.objects.filter(visibility=Post.Visibility.PUBLISHED)

    return render(request, 'list.html', {'blog_posts': blog_posts})


def blog_post_detail(request, slug: str):
    if request.user.is_authenticated:
        blog_post = get_object_or_404(Post, slug=slug)
    else:
        blog_post = get_object_or_404(Post, slug=slug, visibility__in=(
            Post.Visibility.PUBLISHED,
            Post.Visibility.UNLISTED,
        ))

    return render(request, 'post.html', {'blog_post': blog_post})
