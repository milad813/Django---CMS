from django.contrib import admin
from my_app.models import Category, Posts,Authors
# Register your models here.
class Post_admin(admin.ModelAdmin):
    list_display = ('title','counter_view','created_at', 'content')
admin.site.register(Posts,Post_admin)

class Autor_admin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name')
admin.site.register(Authors,Autor_admin)

admin.site.register(Category)
