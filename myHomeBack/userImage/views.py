import json
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from userImage.models import UserImg
from userImage.serializer import UserImgSerializer, SysImgListSerializer
from  AiImageClass.models import AiClass

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework import status
from rest_framework.response import Response

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 30
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'page': self.page.number,
            'page_size': self.page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number # {'page': page_number}

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return None
        return page_number #{'page': page_number}

    # def get_paginated_response(self, data):
    #     return Response({
    #         'count': self.page.paginator.count,
    #         'next': self.get_next_link(),
    #         'previous': self.get_previous_link(),
    #         'page_size': self.page_size,
    #         'results': data
    #     })

class UserImagesView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = UserImgSerializer  # 指定序列化器
    queryset = UserImg.objects.all()  # 指定数据对象查询集
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        '''获取所有图'''
        return self.list(request)

    def post(self, request):
        '''保存图'''
        return self.create(request)
    
    def get_queryset(self):
        '''根据请求参数动态配置 queryset'''
        queryset = UserImg.objects.all()
        # 通过请求参数过滤 queryset
        sys_group_id = self.request.query_params.get('sys_group_id', '1')
        ai_name = self.request.query_params.get('ai_name', '')

        if sys_group_id:
            queryset = queryset.filter(sysGroupId=sys_group_id)
        if len(ai_name) > 0:
            ai_model = AiClass.objects.filter(Q(label__chinese_title__icontains=ai_name) | Q(label__english_title__icontains=ai_name))
            ai_model_values = ai_model.values("image")
            unique_images = set(item['image'] for item in ai_model_values)
            queryset = queryset.filter(image__in = unique_images)
        # 还可以根据其他请求参数进行过滤

        return queryset

class UserImageView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserImgSerializer  # 指定序列化器
    queryset = UserImg.objects.all()  # 指定数据对象查询集

    def get(self, request, pk):
        '''查询单一图片'''
        return self.retrieve(request, pk)

    def put(self, request, pk):
        '''修改图片'''
        print("put", pk)
        
        return self.update(request, pk)
    def delete(self, request, pk):
        '''删除图片'''
        return self.destroy(request,pk)



class ImageListView(CreateModelMixin, GenericAPIView):
    serializer_class = SysImgListSerializer
    
    def create(self, request, *args, **kwargs):
        # 获取请求数据
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 处理请求数据
        self.perform_create(serializer)
        # 返回响应
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        return self.create(request)