from rest_framework import serializers
from sysApp.models import SysGroup


class RecursiveField(serializers.Serializer):
	# 这个类代码保持不变
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class SysGroupTreeSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    children = serializers.ListSerializer(child=RecursiveField())
    class Meta:
        model = SysGroup # 指定根据哪个模型类来序列化
        fields = ('id', 'label', 'children')

class SysGroupSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    class Meta:
        model = SysGroup # 指定根据哪个模型类来序列化
        fields = ('id', 'label', 'parent')

    # def create(self, validated_data):
    #     """新建"""
    #     parent = validated_data.pop('parent')
    #     print(parent)
    #     group = SysGroup.objects.create(validated_data, parent = parent)
    #     return group

    
# class SysGroupImagesSerializer(serializers.ModelSerializer):
#     """元图片数据序列化器"""
#     class Meta:
#         model = SysGroup # 指定根据哪个模型类来序列化
#         fields = ('id', 'label', 'parent')