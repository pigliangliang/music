#author_by zhuxiaoliang
#2018-12-22 下午12:08


from django.urls import path,reverse,re_path

from .views import HomeView,IndexView



app_name='index'





urlpatterns = [

    #path('',IndexView.as_view(),name='index'),
    path('home/<int:id>',HomeView.as_view(),name='home',),

]