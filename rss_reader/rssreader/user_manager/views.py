from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# Create your views here.

def index(request):
    dec = check_error_code(request)
    return render_to_response('index.html', dec, context_instance=RequestContext(request))


def register(request):
    dec = check_error_code(request)
    return render_to_response('register.html', dec, context_instance=RequestContext(request))

def check_error_code(request):
    if request.method == "GET" and request.GET.has_key('error'):
        dec = {"error": str(request.GET['error'])}
    else:
        dec = {}
    return dec

def create_user(request):
    try:
        user_id = request.POST['user_id']
        password = request.POST['password']

        if len(user_id) <= 0 or len(password) <= 0:
            return redirect('/register?error=1')

        elif User.objects.filter(username=user_id):
            return redirect('/index/register?error=2')
        else:
            new_user = User.objects.create_user(username=user_id, email=None, password=password)
            new_user.save()
            return redirect('/index')
    except:
        return redirect('/index/register?error=3')


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
            return redirect('/index?error=1')
    else:
        return redirect('/index?error=2')


def logout(request):
    auth_logout(request)

    return render_to_response('logout.html', {}, context_instance=RequestContext(request))