from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', include('accounts.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('signout/', views.signout_view, name='signout'),
]