import json
from django.http import JsonResponse
from django.views import View
from imagePool.models import SysImg
from imagePool.serializer import SysImgSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.exceptions import ValidationError
from rest_framework import status


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 30


class ImagesView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = SysImgSerializer  # 指定序列化器
    queryset = SysImg.objects.all()  # 指定数据对象查询集
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        '''获取所有图书'''
        return self.list(request)

    def post(self, request):
        '''保存图书'''
        return self.create(request)

class ImageView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = SysImgSerializer  # 指定序列化器
    queryset = SysImg.objects.all()  # 指定数据对象查询集

    def get(self, request, pk):
        '''查询单一图片'''
        return self.retrieve(request, pk)

    def put(self, request, pk):
        '''修改图片'''
        return self.update(request.pk)
    def delete(self, request, pk):
        '''删除图片'''
        return self.destroy(request,pk)


    # def post(self, request):
    #     try:
    #         response = self.create(request)
    #     except ValidationError as e:
    #         errors = e.detail
    #         # 输出错误信息
    #         print(errors)
    #         response = JsonResponse(errors, status=status.HTTP_400_BAD_REQUEST)
    #     print(response)
    #     return response
    
    # def create(self, request):
    #     print("create")
    #     print(request.data)
    #     imgs= request.data.get("img_list")
    #     print(imgs)
    #     serializer = self.get_serializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     return JsonResponse({"a":"he"})