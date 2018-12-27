#author_by zhuxiaoliang
#2018-12-21 下午7:54

from django import forms
from django.contrib.auth.forms import UserCreationForm
from  .models import MyUser




class MyUserForm(UserCreationForm):

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.fields['password1'].widget= forms.PasswordInput(attrs={
            'class': 'txt tabInput',
            'placeholder':'密码,4-16位数字/字母/特殊符号(空格除外)'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'txt tabInput',
            'placeholder':'重复密码'
        })


    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields +('mobile',)
        widgets = {
            'mobile': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '手机号'}),
            'username': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder': '用户名'}),
        }

