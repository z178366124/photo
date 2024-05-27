from django.urls import path
from sysApp.views import SysGroupTreeView, SysGroupView


# 正在部署的应用的名称
app_name = 'sysApp'



urlpatterns = [
    # path函数将url映射到视图
    path('systree/', SysGroupTreeView.as_view(), name='tree'),
    path('grouplists/', SysGroupView.as_view(), name='index'),
    path('grouplists/<int:pk>/', SysGroupView.as_view(), name='sys_group_detail'),  # 单个对象详情视图的 URL
    # path('imglists/<int:pk>/', UserImageView.as_view(), name='index'),
]