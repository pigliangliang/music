from django.shortcuts import render

# Create your views here.
from django.views.generic import View,DetailView
from index.models import Dynamic,Song,Comment,MyUser,SongLabel
from django.urls import reverse
from django.http import HttpResponse

from django.shortcuts import render,redirect

from django.core.paginator import  PageNotAnInteger,Paginator,Page,EmptyPage



class PlayView(DetailView):

    context_object_name = 'song_info'

    pk_url_kwarg = 'pk'
    template_name = 'play.html'

    model = Song

    def get_context_data(self, **kwargs):
        kwargs['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:4]
        # 播放列表
        self.request.session.clear()
        play_list = self.request.session.get('play_list', [])
        song_exist = False
        song_id = self.request.path.split('/')[-2]
        song_exist = False
        if play_list:
            for i in play_list:
                if int(song_id) == i['song_id']:
                    song_exist = True
        if song_exist == False:
            play_list.append(
                {'song_id': int(song_id),
                 'song_singer': self.object.song_singer.singer_name,
                 'song_name': self.object.song_name,
                 })
        self.request.session['play_list'] = play_list
        kwargs['play_list'] = play_list

        #加载歌词
        if self.object.song_lyrics :

            with open(self.object.song_lyrics.path,'r') as f:
                song_lyrics = f.read()

                kwargs['song_lyrics'] = song_lyrics
        else:
            kwargs['song_lyrics'] ='暂无歌词'


        #相关歌曲


        song_relevant = Song.objects.exclude(song_id=song_id).filter(label_id=self.object.label_id)
        print('o',song_relevant)
        kwargs['song_relevant'] = song_relevant





        print(kwargs)
        return super(PlayView,self).get_context_data(**kwargs)




from django.http import StreamingHttpResponse
class Download(View):
    def dispatch(self, request, *args, **kwargs):
        song = Song.objects.filter(song_id=args[0]).first()
        if song.song_album:
            with open(song.song_album,'rb') as f:
                    c = f.read(512)

        filename = str(args[0]) + '.mp3'
        response = StreamingHttpResponse(c)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="%s"' % (filename)
        return response


#歌曲点评

class CommentView(View):

    def get(self,request,song_id):
        search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search')
        contact_all = Comment.objects.filter(song_id=song_id).order_by('-comment_date')
        song_info = Song.objects.filter(song_id=song_id).first()
        song_name = song_info.song_name
        page = request.GET.get('page',1)
        #分页显示
        paginator = Paginator(contact_all, 2)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'comment.html', locals())


    def post(self,request,song_id):

        comments =request.POST.get('comment')
        Comment.objects.create(comment_text=comments,song_id=song_id,comment_user_id=4)

        return redirect(reverse('play:comment',args=song_id))


class Ranking(View):
    def get(self,request):
        search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()

        all_list = SongLabel.objects.distinct()

        type = request.GET.get('type','')
        if type:
            song_info = Dynamic.objects.select_related('song').filter(song__label=type).all()
        else:
            song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()
        print(song_info)
        return render(request,'ranking.html',locals())
