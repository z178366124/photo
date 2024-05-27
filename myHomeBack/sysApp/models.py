from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# from snowflake import Snowflake
# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=128, help_text="用户名", unique=True)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    class Meta:
        indexes = [
            models.Index(fields=["username"], name="username_idx")
        ]

class SysGroup(models.Model):
    label = models.CharField(max_length=50, default="", verbose_name = "组名")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', default=None, blank = True, null=True)
    created = models.DateTimeField(default=timezone.now, verbose_name="图片创建时间")
