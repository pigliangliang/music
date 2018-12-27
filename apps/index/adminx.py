#author_by zhuxiaoliang
#2018-12-22 上午11:29

import xadmin

from index.models import Song,Singer,SongLabel,Dynamic,Comment,UserSong

class SongAdmin(object):
    #显示的列
    list_display = [
        'song_name','song_singer'

    ]

    #搜索的列
    search_fields = [
        'song_name','song_singer'
    ]

    #过滤

    list_filter = [
        'song_name', 'song_singer'
    ]


class SingerAdmin(object):
    list_display= [
        'singer_name','singer_sex','singer_country',
    ]

class SongLabelAdmin(object):
    pass

class DynamicAdmin(object):
    pass

class CommentAdmin(object):
    pass


class UserSongAdmin(object):

    pass



xadmin.site.register(UserSong,UserSongAdmin)

xadmin.site.register(Comment,CommentAdmin)

xadmin.site.register(Dynamic,DynamicAdmin)
xadmin.site.register(Song,SongAdmin)
xadmin.site.register(Singer,SingerAdmin)
xadmin.site.register(SongLabel,SongLabelAdmin)