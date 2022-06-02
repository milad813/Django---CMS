from django.http import HttpResponse
from django.shortcuts import render
from my_app.models import Authors,Posts,Comments,Category

# Create your views here.

def app_home(request):
    return render(request,'my_app/index.html')

def blog_home(request):
    posts=Posts.objects.all()
    return render(request,'my_app/blog_home.html',{'posts':posts})

def blog_post(request,post_id):
    post=Posts.objects.get(id=post_id)

    return render(request,'my_app/blog_post.html',{'post':post})
    