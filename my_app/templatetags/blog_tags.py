from django import template
from my_app.models import *


register = template.Library()


@register.inclusion_tag('my_app/includes/category_count_sidebar.html')
def category_list():
	categories=Category.objects.all()
	posts=Post.objects.filter(is_active=True)
	my_dict={}
	for cat in categories:
		my_dict[cat]=posts.filter(category__name=cat).count()
	return {'categories':my_dict}


@register.filter
def snippet(value):

	return ' '.join(value.split()[:10]) + '...'

@register.inclusion_tag('my_app/includes/latest_posts_tag.html')
def latest_posts(count=5):
	posts=Post.objects.filter(is_active=True)
	return {'posts':posts[:count]}