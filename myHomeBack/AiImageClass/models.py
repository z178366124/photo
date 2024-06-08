from django.db import models
# from imagePool.models import SysImg
from django.utils import timezone
# Create your models here.

class AiClassTitle(models.Model):
    # 创建时间
    chinese_title = models.CharField(max_length=64, verbose_name="中文名")
    english_title = models.CharField(max_length=64, verbose_name="英文名")

class AiClass(models.Model):
    image = models.ForeignKey("imagePool.SysImg", on_delete=models.CASCADE, verbose_name="图片")
    label = models.ForeignKey(AiClassTitle, on_delete=models.CASCADE, verbose_name="标签")
    locationX1 = models.FloatField(verbose_name="位置坐标，X1")
    locationY1 = models.FloatField(verbose_name="位置坐标，y1")
    locationX2 = models.FloatField(verbose_name="位置坐标，X2")
    locationY2 = models.FloatField(verbose_name="位置坐标，y2")
    created = models.DateTimeField(default=timezone.now, verbose_name="图片创建时间")
    class Meta:
        ordering = ['-created']
    def __str__(self) -> str:
        return self.label