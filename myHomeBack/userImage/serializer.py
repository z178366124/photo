from rest_framework import serializers
from userImage.models import UserImg
from imagePool.models import SysImg
from imagePool.serializer import SysImgSerializer
from sysApp.models import SysGroup
# from django.db import models

def validate_file(value):
    print("文件校验器")
    return
    # if value is None:
    #     raise serializers.ValidationError("上传的文件不能为空")

class UserImgSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    img = serializers.ImageField(write_only = True, required=False)
    # image = serializers.PrimaryKeyRelatedField(read_only=True)
    image = SysImgSerializer(read_only = True)
    # sysGroupId = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserImg # 指定根据哪个模型类来序列化
        fields = ('name', 'describe', 'img', 'image', 'sysGroupId')

    def create(self, validated_data):
        """新建"""

        image_data = validated_data.pop('img')
        
        # 创建图像对象
        image = SysImg.create_with_hash(image_data = image_data)
        
        # # 创建用户图片对象，并将图像对象关联到用户图片中
        user_img = UserImg.objects.create(image=image, **validated_data)
        return user_img

class SysImgListSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    img_list = serializers.ListField(child=serializers.ImageField(), write_only = True)
    group_id = serializers.IntegerField(write_only = True)
    a = SysImgSerializer(read_only = True)

    class Meta:
        model = SysImg # 指定根据哪个模型类来序列化
        fields = ('img_list', 'group_id', "a")
    

    def create(self, validated_data):
        """新建"""
        images_data = validated_data.pop('img_list')
        group_id = validated_data.pop("group_id")
        
        try:
            group = SysGroup.objects.get(pk=group_id)
        except SysGroup.DoesNotExist:
            print("Group does not exist.")
            return None

        images = []
        
        for image_data in images_data:
            image = SysImg.create_with_hash(image_data=image_data)
            user_img = UserImg.objects.create(image=image, sysGroupId=group)
            images.append(user_img)
        
        return images

    def to_representation(self, instance):#  存在问题，放弃解决
        # 将 SysImg 对象列表转换为字典列表，使用 SysImgSerializer 进行序列化
        t= SysImgSerializer(instance, many=True).data
        return {}
