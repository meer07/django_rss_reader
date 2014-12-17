from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):

    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def register(request):
    return render_to_response('register.html', {}, context_instance=RequestContext(request))

def create_user(request):
    try:
        user_id = request.POST['user_id']
        password = request.POST['password']

        if len(user_id) <= 0 or len(password) <= 0:


        elif User.objects.filter(username=user_id):
            return render_to_response('register.html', {"error":"2"}, context_instance=RequestContext(request))
        else:
            new_user = User.objects.create_user(username=user_id, email=None, password=password)
            new_user.save()
            return redirect('/index')
    except:
        return redirect('/register')




def login(request):
    user_id = request.POST['user_id']
    password = request.POST['password']

    user = authenticate(username=user_id, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            user_page_url = '/user/?user_id=' + user_id
            return redirect(user_page_url)
        else:
            return HttpResponseRedirect(index,args=[])
    else:
        return render_to_response('index.html', {"error": "2"}, context_instance=RequestContext(request))
