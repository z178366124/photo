from django.db import models
from django.utils import timezone
from imagePool.models import SysImg
from sysApp.models import SysGroup,User


class UserImg(models.Model):
    # id = models.BigIntegerField(primary_key=True, verbose_name= "id(雪花id)")
    name = models.CharField(max_length=100, verbose_name= "资源名字", default="", blank=True, null=True)
    image = models.ForeignKey(SysImg, on_delete=models.CASCADE)
    describe = models.CharField(max_length=200, verbose_name= "图片描述", default= "")
    created = models.DateTimeField(default=timezone.now, verbose_name="图片创建时间")
    sysGroupId = models.ForeignKey(SysGroup, on_delete=models.CASCADE, related_name='sysgroupid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=None, blank = True, null=True)

    def copy(self, obj: SysImg):
        if not self.name:
            self.name = obj.name
        self.image = obj.copy()
        return self
    
    def ref_delete(self):
        self.image.ref_delete()
        self.delete()
    class Meta:
        ordering = ['-created']