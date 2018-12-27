from django.db import models

# Create your models here.

from  django.contrib.auth.models import AbstractUser

from datetime import datetime




class MyUser(AbstractUser):
    qq = models.CharField('QQ',max_length=20)
    webChat = models.CharField('微信',max_length=20)
    mobile = models.CharField('手机号',max_length=20,unique=True)

    class Meta:
        verbose_name  = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username

