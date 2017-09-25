# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_img',
            name='blog_img',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='blog_img',
            name='blog_img_id',
            field=models.CharField(primary_key=True, max_length=64, serialize=False),
        ),
    ]
