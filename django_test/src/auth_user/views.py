import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_user(request):
    if request.method =="GET":
        return render(request, template_name="auth_user/login.html")
    elif request.method =="POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        print(user, password)
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request,user)
            next = request.GET.get("next")
            if next is not None:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect("/")
        5/0

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")