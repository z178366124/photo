import json
from django.http import JsonResponse
from django.views import View
from .serializer import AiClassTitleSerializer, AiClassSerializer
from .models import AiClass
from django.db.models import Q

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
        return page_number

class UserImagesView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = AiClassSerializer  # 指定序列化器
    queryset = AiClass.objects.all()  # 指定数据对象查询集
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        '''获取组别'''
        return self.list(request)

    def post(self, request):
        '''保存图类'''
        return self.create(request)

    def get_queryset(self):
        '''根据请求参数动态配置 queryset'''
        queryset = AiClass.objects.all()
        # 通过请求参数过滤 queryset
        # sys_group_id = self.request.query_params.get('sys_group_id', None)

        # if sys_group_id == '1':
        #     return queryset

        # if sys_group_id:
        #     queryset = queryset.filter(sysGroupId=sys_group_id)
        # 还可以根据其他请求参数进行过滤
        queryset = queryset.filter(Q(label__chinese_title__icontains='person') | Q(label__english_title__icontains='person'))
        return queryset

class UserImageView(GenericAPIView, UpdateModelMixin):
    serializer_class = AiClassSerializer  # 指定序列化器
    queryset = AiClass.objects.all()  # 指定数据对象查询集

    def get(self, request, pk):
        '''查询单图单类'''
        return self.retrieve(request, pk)
        
        return self.update(request, pk)
    def delete(self, request, pk):
        '''删除图片'''
        return self.destroy(request,pk)