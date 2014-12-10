#coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def user_page(request):
    user_id = request.POST['user_id']

    # 設定を全て読み出す。
    # rssをパースして新着順にする

    return render_to_response('user_page.html',{},context_instance=RequestContext(request))