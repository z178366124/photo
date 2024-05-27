# Generated by Django 5.0.4 on 2024-05-27 11:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='photo/%Y-%m-%d/')),
                ('reference_count', models.IntegerField(default=1, verbose_name='引用计数器')),
                ('hash_value', models.CharField(blank=True, max_length=64)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='图片创建时间')),
            ],
        ),
    ]
