#author_by zhuxiaoliang
#2018-12-21 下午8:08

from django.urls import path,re_path
from .views import Login,Register,Logout

app_name = 'user'



urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),

]