from django.db import models

# Create your models here.
from datetime import datetime
from user.models import MyUser

#歌曲分类
class SongLabel(models.Model):
    label_id = models.AutoField('序号',primary_key=True)
    label_name = models.CharField('分类标签',max_length=32)

    class Meta:
        verbose_name='歌曲分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label_name



#歌曲信息
class Song(models.Model):
    song_id = models.AutoField("歌曲序号",primary_key=True)
    song_name =models.CharField('歌曲名字',max_length=32)
    song_singer = models.ForeignKey('Singer',on_delete=models.CASCADE,verbose_name='歌手')
    song_album = models.CharField('专辑', max_length=50)
    song_languages = models.CharField('语种', max_length=20)
    song_release = models.DateField('发行时间', default=datetime.now)
    song_img = models.ImageField('歌曲图片', upload_to='img/%Y%m',max_length=100,blank=True)
    song_lyrics = models.FileField('歌词', upload_to='file/%Y%m',blank=True)
    label = models.ForeignKey(SongLabel, on_delete=models.CASCADE, verbose_name='歌名分类')
    def __str__(self):
        return self.song_name

    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'

class Singer(models.Model):

    SINGER_SEX=(
        ('1','男'),
        ('2','女'),

    )

    SINGER_COUNTRY = (
        ('1','大陆'),
        ('2','港台'),
        ('3','岛国'),
        ('4','欧美'),

    )

    singer_name = models.CharField('歌手名字',max_length=32)
    singer_sex = models.CharField('歌手性别',choices=SINGER_SEX,max_length=100)
    singer_country = models.CharField('歌手国籍',choices=SINGER_COUNTRY,max_length=100)
    singer_image= models.ImageField('歌手照片',upload_to='image/%Y%m',default='music/static/image/datu-1.jpg',max_length=100,null=True, blank=True)

    class Meta:
        verbose_name ='歌手'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.singer_name

#歌曲动态

class Dynamic(models.Model):
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌曲')
    dynamic_plays = models.IntegerField('播放次数')
    dynamic_search = models.IntegerField('搜索次数')
    dynamic_down = models.IntegerField('下载次数')

    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲动态'
        verbose_name_plural = '歌曲动态'

    def __str__(self):
        return '{}播放次数{}'.format(self.song.song_name,self.dynamic_plays)


# 歌曲点评表comment
class Comment(models.Model):
    comment_id = models.AutoField('序号', primary_key=True)
    comment_text = models.CharField('内容', max_length=500)
    comment_user = models.ForeignKey(MyUser, on_delete=models.CASCADE,verbose_name='用户')
    song = models.ForeignKey(Song, on_delete=models.CASCADE,verbose_name='歌名')
    comment_date = models.CharField('日期', default=datetime.now,max_length=100)
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲评论'
        verbose_name_plural = '歌曲评论'


    def __str__(self):
        return self.comment_text


class UserSong(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='用户')
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='我的歌曲')
    add_time=models.DateField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户歌曲'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '{}收听歌曲：{}'.format(self.user.username,self.song.song_name)
