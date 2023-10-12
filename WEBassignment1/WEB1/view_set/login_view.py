from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse

def longin_v(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active == True:
                login(request,user)#一段时间内浏览器会记住账号密码
                return render(request,'index.html')
            else:
                return HttpResponse('error')


def logout_v(request):
    logout(request)
    return redirect('login')


def welcome(request):
    return render(request,'welcome.html')