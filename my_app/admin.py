from django.contrib import admin

from my_app.models import Category, Posts,Authors,Comments,Tag
# Register your models here.
class Post_admin(admin.ModelAdmin):
    list_display = ('title','counter_view','created_at', 'content')
    list_filter = ('created_at',)
    search_fields = ('title','content')
    ordering = ('-created_at',)
    fields = ('title','content','images','counter_view','author','category','tags','comments')




admin.site.register(Posts,Post_admin)

class Autor_admin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name')
admin.site.register(Authors,Autor_admin)

admin.site.register(Category)
admin.site.register(Tag)


class Comment_admin(admin.ModelAdmin):
    list_display = ('name','email','content','created_at')

    
admin.site.register(Comments,Comment_admin)

