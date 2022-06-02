from django.urls import path
from . import views

app_name='my_app'

urlpatterns=[
    path('',views.app_home,name='app_home'),
    path('blog/',views.blog_home,name='blog_home'),
    path('blog/<int:post_id>/',views.blog_post,name='blog_post'),
]