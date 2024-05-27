from django.urls import path
from imagePool.views import ImagesView,ImageView

# 正在部署的应用的名称
app_name = 'imagePool'



urlpatterns = [
    # path函数将url映射到视图
    path('lists/', ImagesView.as_view(), name='index'),
    path('lists/<int:pk>/', ImageView.as_view(), name='index'),
]