# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=100, verbose_name='\u30e6\u30fc\u30b6\u30fcID')),
                ('feed_site_url', models.CharField(max_length=100, verbose_name='\u767b\u9332url')),
                ('feed_site_name', models.CharField(max_length=100, verbose_name='\u30b5\u30a4\u30c8\u540d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
