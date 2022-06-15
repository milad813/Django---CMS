from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from my_app.forms import ContactForm
from my_app.models import Authors, Category, Comments, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/accounts/login/')
def blog_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_active=True)
    post.counter_view += 1
    post.save()

    return render(request, 'my_app/blog_post.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return render(request, 'my_app/contact.html')
        else:
            messages.error(request, 'Your message has not been sent!')
            return render(request, 'my_app/blog_home.html')
    return render(request, 'my_app/contact.html')