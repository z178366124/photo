from django.urls import path
from .views import UserImagesView

# 正在部署的应用的名称
app_name = 'AiImageClass'



urlpatterns = [
    # path函数将url映射到视图
    path('ailist/', UserImagesView.as_view(), name='index'),
    path('ailist/<int:pk>/', UserImagesView.as_view(), name='index'),
]