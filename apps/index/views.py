from django.shortcuts import render

# Create your views here.
from .models import Dynamic
from django.views.generic import View,ListView,DetailView
from django.core.paginator import Page,Paginator,PageNotAnInteger,EmptyPage
from index.models import UserSong,SongLabel,Song

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required





class HomeView(ListView):

    model = Dynamic
    context_object_name = 'search_song'
    template_name = 'home.html'
    paginate_by = 2



    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView,self).dispatch(request,*args,**kwargs)

    def get_queryset(self):
        return Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:4]

    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.request.path.split('/')[-1])
        print(self.request.user.id)
        print(self.request.GET.get('id'))
        contacts = UserSong.objects.select_related('song').filter(user_id=self.request.user.id)
        paginator = Paginator(contacts, 3)
        try:

            contacts = paginator.page(self.request.path.split('/')[-1])
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        kwargs['contacts'] =contacts

        return super(HomeView,self).get_context_data(**kwargs)


class IndexView(View):
    def get(self,request):
        # 热搜歌曲
        search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:8]
        # 音乐分类
        label_list = SongLabel.objects.all()
        # 热门歌曲
        play_hot_song = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
        # 新歌推荐
        daily_recommendation = Song.objects.order_by('-song_release').all()[:3]
        # 热门搜索、热门下载
        search_ranking = search_song[:6]
        down_ranking = Dynamic.objects.select_related('song').order_by('-dynamic_down').all()[:6]
        all_ranking = [search_ranking, down_ranking]
        return render(request, 'index.html', locals())

