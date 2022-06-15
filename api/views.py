import json
from django.forms import model_to_dict
from django.http import JsonResponse
from my_app.models import Post
from rest_framework.response import Response

# Create your views here.

def index(request, *args, **kwargs):
    # params=request.GET
    # data=request.body
    # data=json.loads(data)
    # print(type(params))
    model_data=Post.objects.filter(is_active=True).first()
    data = model_to_dict(model_data,exclude=['images','comments','category','tags','author'])
    return JsonResponse(data)