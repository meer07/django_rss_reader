#coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponse, redirect
from user_page.models import Feed
from user_page.feed_parser import feed_passer
import json


# Create your views here.
# ユーザーページ初期表示
def user_page(request):
    user_id = str(request.GET['user_id'])
    sites = Feed.objects.filter(user_id=user_id)
    # 設定を全て読み出す。
    return render_to_response('user_page.html', {'site_items': sites, 'user_id': user_id}, context_instance=RequestContext(request))

# 追加したurlを保存する
def save_url(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        url = request.POST['url']
        site_name = request.POST['site_name']

        feed = Feed(user_id=user_id, feed_site_url=url, feed_site_name=site_name)
        feed.save()

        return redirect("/user/?user_id="+user_id)



# urlを取得してfeedを収集してjsonで送り返す
def read_feed(request):
    if request.method == 'POST':
        url = request.POST['url']
        print url
        passer = feed_passer(feed_url=url)
        response = json.dumps({'feed': passer.feed_list}, indent=2)
        return HttpResponse(response, content_type='application/json; charset=UTF-8')