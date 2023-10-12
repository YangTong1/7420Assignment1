from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *

@login_required
@permission_required('auth.add_user',raise_exception=True)
def add_user(request):
    if request.method == "GET":
        return render(request,'add_user.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        telephone = request.POST['telephone']
        address = request.POST['address']
        group = request.POST['select_group']

        try:
            myuser = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
            #myuser.save()
            UserProfile.objects.create(user=myuser,address=address,telephone=telephone)
            if group == '0':
                gp = Group.objects.get(name='Admin')
            elif group == '1':
                gp = Group.objects.get(name='Lecturer')
            elif group == '2':
                gp = Group.objects.get(name='Student')
            print(f'gp:{gp}')
            myuser.groups.add(gp)
            myuser.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')


@login_required
@permission_required('auth.view_user',raise_exception=True)
def select_user(request):
    if request.method == 'GET':
        users = UserProfile.objects.all()
        #uplist = []
        # for u in users:
        #     up = UserProfile.objects.get(user__username=u.username)
        #     uplist.append(up)
        return render(request,'select_user.html',{'users':users})


@login_required
@permission_required('auth.change_user',raise_exception=True)
def change_user(request):
    if request.method == 'GET':
        username = request.GET['username']
        myuser = User.objects.get(username=username)
        up = UserProfile.objects.get(user=myuser)
        return render(request,'change_user.html',{'myuser':myuser,'up':up})

    elif request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        telephone = request.POST['telephone']
        address = request.POST['address']
        group = request.POST['select_group']

        try:
            myuser = User.objects.get(username=username)
            myuser.email = email
            myuser.first_name = fname
            myuser.last_name = lname
            if group == '0':
                gp = Group.objects.get(name='Admin')
            elif group == '1':
                gp = Group.objects.get(name='Lecturer')
            elif group == '2':
                gp = Group.objects.get(name='Student')
            myuser.groups.set([gp])#set方法要列表
            myuser.save()
            up = UserProfile.objects.get(user=myuser)
            up.address = address
            up.telephone = telephone
            up.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')


@login_required
@permission_required('auth.delete_user',raise_exception=True)
def delete_user(request):
    if request.method == 'GET':
        getusername = request.GET['username1']
        U = User.objects.get(username=getusername)
        U.delete()
        return redirect('/select_user/')
