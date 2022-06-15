from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
]
