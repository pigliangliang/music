from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
# Create your views here.

def index(request):
    type_list = product.objects.values('type').distinct()
    name_list = product.objects.values('name','type')
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html',context=context, status=200)

