from django.urls import path
from . import views

app_name = 'accounts'

url_patterns = [
    # path('', include('accounts.urls')),
    # path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    # path('signout/', views.signout, name='signout'),
]