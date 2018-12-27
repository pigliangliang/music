#author_by zhuxiaoliang
#2018-12-23 下午11:12
from  django.urls import path,re_path
from .views import PlayView,Download,CommentView,Ranking



app_name = 'play'

urlpatterns =[

    path('<int:pk>/',PlayView.as_view(),name='play_song'),
    re_path('download/(\d+)',Download.as_view(),name='download'),
    path('comment/<str:song_id>/',CommentView.as_view(),name='comment'),
    path('ranking/',Ranking.as_view(),name='ranking')
]