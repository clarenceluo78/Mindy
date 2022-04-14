from django.urls import path

from .views.views import *
from .views.login import *

# 子路由文件
urlpatterns = [
    # path('', login, name='web_login'),
    path('', to_list, name='home_list'),  # 跳转列表界面
    path('login/', login, name='web_login'),
    path('register/', register),
    path('logout/', logout),
    path('confirm/', user_confirm),
    path('detail/', to_detail),  # 跳转详情界面
    path('create/', JsMindView.as_view()),  # 创建思维导图
    path('delete/', JsMindView.as_view()),  # 删除思维导图
    path('list/', JsMindView.as_view()),  # 查询思维导图
    path(r'jsmind_op', JsMindLogView.as_view()),  # 更新快照，get日志
]
