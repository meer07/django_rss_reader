#coding:utf-8
from django.db import models

# Create your models here.
class Feed(models.Model):
    user_id = models.CharField(u"ユーザーID", max_length=100)
    feed_site_url = models.CharField(u"登録url", max_length=100)
    feed_site_name = models.CharField(u"サイト名", max_length=100)

    def __str__(self):
        return self.feed_site_name