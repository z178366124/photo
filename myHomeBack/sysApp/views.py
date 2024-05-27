import json
from django.http import JsonResponse
from django.views import View
from sysApp.models import SysGroup
from sysApp.serializer import SysGroupTreeSerializer, SysGroupSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status

class SysGroupTreeView(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = SysGroupTreeSerializer  # 指定序列化器
    queryset = SysGroup.objects.all()  # 指定数据对象查询集
    # pagination_class = LargeResultsSetPagination

    def get(self, request, format=None):
        # 获取根节点
        root_groups = SysGroup.objects.filter(parent=None)
        
        # 序列化数据
        serializer = SysGroupTreeSerializer(instance=root_groups, many=True)
        
        return Response(serializer.data)
        

class SysGroupView(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericAPIView):
    serializer_class = SysGroupSerializer  # 指定序列化器
    queryset = SysGroup.objects.all()  # 指定数据对象查询集
    # pagination_class = LargeResultsSetPagination

    def get(self, request):
        '''获取所有图书'''
        return self.list(request)

    def post(self, request):
        '''保存图书'''
        return self.create(request)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status = status.HTTP_204_NO_CONTENT)

    