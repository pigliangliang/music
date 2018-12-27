from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
from django.views.generic import View

from .forms import MyUserForm
from .models import MyUser
from django.contrib.auth import authenticate,login,logout
from index.models import Dynamic


class Login(View):
    def get(self,request):
        return render(request, 'login.html', locals())
    def post(self,request):
        user = request.POST.get('username')
        password = request.POST.get('password')
        print(user,password)
        u = authenticate(username=user,password=password)

        if u:
            login(request,u)
            return redirect(reverse('index:home',args=[1,]))
        else:
            tips='用户名或密码错误'
            return render(request, 'login.html', locals())



class Register(View):
    def get(self,request):
        user = MyUserForm()
        return render(request, 'register.html', locals())
    def post(self,request):
        user = MyUserForm(request.POST)
        if user.is_valid():
            user.save()
            return  render(request, 'login.html', locals())
        else:
            tips = user.errors

            return render(request, 'register.html', locals())


class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('user:login'))


