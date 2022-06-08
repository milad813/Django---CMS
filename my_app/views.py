from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from my_app.forms import CommentForm
from my_app.models import Authors, Category, Post

# Create your views here.


def app_home(request):
    return render(request, 'my_app/index.html')


def blog_home(request, **kwargs):
    posts = Post.objects.filter(is_active=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        

    if kwargs.get('category_name'):
        posts = posts.filter(category__name=kwargs['category_name'])
    if kwargs.get('author_name'):
        posts = posts.filter(author__username=kwargs['author_name'])
    if querry := request.GET.get('search'):
        posts = posts.filter(content__icontains=querry)
    return render(request, 'my_app/blog_home.html', {'posts': posts})


def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_active=True)

    return render(request, 'my_app/blog_post.html', {'post': post})
