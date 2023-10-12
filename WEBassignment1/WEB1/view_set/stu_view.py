from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *
from django.core.mail import send_mail


@login_required
@permission_required('WEB1.add_student',raise_exception=True)
def add_student(request):
    if request.method == "GET":
        return render(request,"add_student.html")
    elif request.method == "POST":
        student_id = request.POST['student_id']
        DOB = request.POST['DOB']
        attend = request.POST['attend']
        username = request.POST['username']
        course = request.POST['course']
        print(course)

        c = course.split(',')#按照逗号分隔字符串
        course_include = Course.objects.filter(name__in=c)
        #当前C时一个包含所有添加课程的列表，通过遍历C搜索课程可以获取课程名字，通过名字查询对象，纳入student里面
        #c[0] ="C#"
        #Course.objects.get(name=c[0])#都取用name__in
        print(c)
        try:
            myuser = User.objects.get(username=username)
            stu = Student.objects.create(student_id=student_id,DOB=DOB,attend=attend,user=myuser)
            stu.course.add(*course_include)
            return HttpResponse('Add Successfully')
        except Exception as e:
            print(e)
            return HttpResponse("error")


@login_required
@permission_required('WEB1.view_student',raise_exception=True)
def select_student(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        return render(request,'select_student.html',{'stu':stu})


@login_required
@permission_required('WEB1.change_student',raise_exception=True)
def change_student(request):
    if request.method == 'GET':
        sid = request.GET['cid']
        stu = Student.objects.get(student_id=sid)
        users = User.objects.all()
        myuser = stu.user
        courses = Course.objects.all()
        mycourse = stu.course.all()
        check_id = []
        for i in mycourse:
            check_id.append(i.id)
        return render(request,'change_student.html',{'stu':stu,'users':users,'myuser':myuser,'courses':courses,'check_id':check_id})

    elif request.method == 'POST':
        getid = request.POST['student_id']
        attend = request.POST['attend']
        DOB = request.POST['DOB']
        usertags = request.POST.getlist('tags')
        coursetags = request.POST.getlist('coursetags')
        try:
            stu = Student.objects.get(student_id=getid)
            stu.DOB = DOB
            stu.attend = attend
            if len(usertags) > 1:
                return HttpResponse('username only choose one')
            myuser = User.objects.get(username=usertags[0])
            stu.user = myuser
            stu.course.set(coursetags)
            stu.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')



@login_required
@permission_required('WEB1.delete_student',raise_exception=True)
def delete_student(request):
    if request.method == 'GET':
        getid = request.GET['did']
        try:
            s = Student.objects.get(student_id=getid)
            s.delete()
            return redirect('/select_student/')
        except Exception as e:
            print(e)
            return HttpResponse('error')


@login_required
@permission_required('WEB1.change_student',raise_exception=True)
def send_email(request):
    if request.method == 'GET':
        sid = request.GET['id']
        stu = Student.objects.get(student_id=sid)
        return render(request,'send.html',{'stu':stu})
    elif request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        to = request.POST['to']
        try:
            send_mail(subject=subject, message=content, recipient_list=[to,], from_email="ferrari430tong@gmail.com")
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')

@login_required
@permission_required('AttSystem.view_student', raise_exception=True)
def stu_class(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        return render(request, 'stu_class.html', {"stu":stu})


@login_required
@permission_required('AttSystem.change_student', raise_exception=True)
def enroll(request):
    if request.method == 'GET':
        sid = request.GET.get("id")
        stu = Student.objects.get(student_id=sid)
        myclass = stu.myclass.all()
        classes = Class.objects.all()
        check_id = []
        for i in myclass:
            check_id.append(i.id)
        return render(request, 'enroll.html', {"stu":stu, "classes":classes, "check_id":check_id})
    elif request.method == 'POST':
        sid = request.POST.get("stu_id")
        classtags = request.POST.getlist("ctags")
        try:
            stu = Student.objects.get(student_id=sid)
            stu.myclass.set(classtags) #coursetags是id列表 或者传对象列表
            stu.save()
            return HttpResponse("ok")
        except Exception as e:
            print(e)
            return HttpResponse("error")
