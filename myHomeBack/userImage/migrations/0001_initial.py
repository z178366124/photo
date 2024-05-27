# Generated by Django 5.0.4 on 2024-05-27 11:05

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imagePool', '0001_initial'),
        ('sysApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='资源名字')),
                ('describe', models.CharField(default='', max_length=200, verbose_name='图片描述')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='图片创建时间')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagePool.sysimg')),
                ('sysGroupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sysgroupid', to='sysApp.sysgroup')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]