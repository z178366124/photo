from rest_framework import serializers
from .models import AiClassTitle, AiClass
# from django.db import models


class AiClassTitleSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    class Meta:
        model = AiClassTitle # 指定根据哪个模型类来序列化
        fields = ('id', 'chinese_title', 'english_title')

class AiClassSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    class Meta:
        model = AiClass # 指定根据哪个模型类来序列化
        fields = ('id', 'image', 'label', 'locationX1', "locationY1", 'locationX2', "locationY2")
