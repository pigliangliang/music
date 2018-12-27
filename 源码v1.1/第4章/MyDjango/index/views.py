from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
import csv
# Create your views here.

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response

def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html',context=context, status=200)

# locals()使用技巧
# def index(request):
#     type_list = Product.objects.values('type').distinct()
#     name_list = Product.objects.values('name','type')
#     title = '首页'
#     return render(request, 'index.html',context=locals(), status=200)

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # 相对路径，代表首页地址
        return redirect('/')
        # 绝对路径，完整的地址信息
        # return redirect('http://127.0.0.1:8000/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('username is '+ name)


# 通用视图
from django.views.generic import ListView
class ProductList(ListView):
    # context_object_name设置Html模版的变量名称
    context_object_name = 'type_list'
    # 设定HTML模版
    template_name='index.html'
    # 查询数据
    queryset = Product.objects.values('type').distinct()

    # 重写 get_queryset 方法，对模型product进行数据筛选。
    def get_queryset(self):
        # 获取URL的变量id
        print(self.kwargs['id'])
        # 获取URL的参数name
        print(self.kwargs['name'])
        # 获取请求方式
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list

    # 添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name','type')
        return context