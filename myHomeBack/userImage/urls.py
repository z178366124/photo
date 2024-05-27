from django.urls import path
from userImage.views import UserImagesView,UserImageView, ImageListView


# 正在部署的应用的名称
app_name = 'userImage'



urlpatterns = [
    # path函数将url映射到视图
    path('albums/', UserImagesView.as_view(), name='index'),
    path('albums/<int:pk>/', UserImageView.as_view(), name='index'),
    path('albums/upload/', ImageListView.as_view(), name='index'),

]