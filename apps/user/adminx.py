#author_by zhuxiaoliang
#2018-12-22 上午11:25

import xadmin
from xadmin import views


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '后台管理界面'
    # 修改footer
    site_footer = '未来网络高精尖中心'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
