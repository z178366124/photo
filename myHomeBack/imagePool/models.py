from django.db import models
from django.utils import timezone
import hashlib
import os
# from snowflake import Snowflake
# Create your models here.


class SysImg(models.Model):
    # 创建时间
    # id = models.BigIntegerField(primary_key=True, verbose_name= "id(雪花id)")
    # src = models.CharField(max_length=200, default="", verbose_name = "资源路径")
    img = models.ImageField(upload_to='photo/%Y-%m-%d/', blank=True)
    reference_count = models.IntegerField(default=1, verbose_name="引用计数器")
    hash_value = models.CharField(max_length=64, blank=True)  # 存储图片的sha256值的字段
    created = models.DateTimeField(default=timezone.now, verbose_name="图片创建时间")

    def copy(self):
        self.reference_count +=1
        return self
    
    def ref_delete(self):
        self.reference_count -=1
        if self.reference_count == 0:
            self.delete()

    
    def save(self, *args, **kwargs):
        if not self.pk and self.img :  # 如果对象尚未保存到数据库中
            # 计算图片的SHA-256值
            sha256_hash = hashlib.sha256()
            for chunk in self.img.chunks():
                sha256_hash.update(chunk)
            self.hash_value = sha256_hash.hexdigest()

            # 在保存之前检查是否存在相同的哈希值
            existing_objs = SysImg.objects.filter(hash_value=self.hash_value)
            if existing_objs.exists():  # 如果存在相同的哈希值的对象，则返回该对象
                return existing_objs.first()

            # 使用哈希值作为文件名的一部分
            filename, extension = os.path.splitext(self.img.name)
            new_filename = f"{self.hash_value}{extension}"
            self.img.name = os.path.join('photo', timezone.now().strftime("%Y-%m-%d"), new_filename)

        super().save(*args, **kwargs)

    @classmethod
    def create_with_hash(cls , image_data):
        if image_data:  # 如果对象尚未保存到数据库中
            # 计算图片的SHA-256值
            sha256_hash = hashlib.sha256()
            for chunk in image_data.chunks():
                sha256_hash.update(chunk)
            hash_value = sha256_hash.hexdigest()

            # 在保存之前检查是否存在相同的哈希值
            existing_objs = SysImg.objects.filter(hash_value=hash_value)
            if existing_objs.exists():  # 如果存在相同的哈希值的对象，则返回该对象
                return existing_objs.first()
            
            # 如果不存在相同哈希值的图片对象，则创建一个新的图片对象
            img_obj = cls.objects.create(img=image_data)
            return img_obj