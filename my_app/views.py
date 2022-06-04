from django.shortcuts import get_object_or_404, render

from my_app.models import Authors, Category, Comments, Post

# Create your views here.


def app_home(request):
    return render(request, 'my_app/index.html')


def blog_home(request):
    posts = Post.objects.filter(is_active=True)
    return render(request, 'my_app/blog_home.html', {'posts': posts})


def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_active=True)

    return render(request, 'my_app/blog_post.html', {'post': post})

def blog_category(request, category_name):
    posts = Post.objects.filter(category__name=category_name, is_active=True)
    return render(request, 'my_app/blog_home.html', {'posts': posts})
