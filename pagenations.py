#author_by zhuxiaoliang
#2018-12-22 下午5:28
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView


class Page:
    def __init__(self,per_page_nums,queryset):
        self.queryset=queryset
        self.num_per_nums = per_page_nums



    def previous(self):

        pass

    def current(self):
        pass

    def next(self):
        pass

