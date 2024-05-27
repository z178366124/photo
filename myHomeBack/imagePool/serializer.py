from rest_framework import serializers
from imagePool.models import SysImg


class SysImgSerializer(serializers.ModelSerializer):
    """元图片数据序列化器"""
    # imgs = serializers.ListField(child=serializers.ImageField(), write_only = True)
    # img = serializers.ImageField(read_only = True)
    class Meta:
        model = SysImg # 指定根据哪个模型类来序列化
        fields = ('img',)
        # fields = '__all__'

    def create(self, validated_data):
        """新建"""
        # print()
        image = SysImg(**validated_data)
        image.save()
        return image
    


# class SysImgListSerializer(serializers.Serializer):
#     """元图片数据序列化器"""
#     img_list = serializers.ListField(child=serializers.ImageField(), write_only = True)

#     def create(self, validated_data):
#         """新建"""
#         print("-------------------------\n")
#         images_data = validated_data.pop('img_list')
#         images = []
#         t = None
#         for image_data in images_data:
#             image = SysImg(img=image_data)
#             image.save()
#             images.append(image)
#             t = image
#             print(image)
#         return t