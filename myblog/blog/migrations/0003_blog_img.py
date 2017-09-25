# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170801_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_img',
            fields=[
                ('blog_img_id', models.IntegerField(primary_key=True, serialize=False)),
                ('blog_img', models.FileField(upload_to='./static/img/')),
            ],
        ),
    ]
