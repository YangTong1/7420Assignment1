from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect,HttpResponse
from .models import *
# Create your views here.

@login_required #decorator,装饰器 限制必须登录后访问
def index(request):
    return render(request,'index.html')
@login_required
@permission_required('WEB1.add_course')#参数是去django里面匹配admin——permission权限
def add_course(request):
    if request.method == "GET":
        return render(request,"add_course.html")
    elif request.method == "POST":
        course_code = request.POST['course_code']
        course_name = request.POST['course_name']

        Course.objects.create(code=course_code,name=course_name)
        message = "Add successfully"
        return render(request,"add_course.html",{"message":message})

def add_lecturer(request):
    if request.method == "GET":
        return render(request,"add_lecturer.html")
    elif request.method == "POST":
        staff_id = request.POST['staff_id']
        DOB = request.POST['DOB']
        username = request.POST['username']

        try:
            myuser = User.objects.get(username=username)
            Lecturer.objects.create(staff_id=staff_id,DOB=DOB,user=myuser)
        except Exception as e:
            print(e)
            return HttpResponse("error")
        return HttpResponse("ok")

def add_semester(request):
    if request.method == "GET":
        return render(request,'add_semester.html')
    elif request.method == "POST":
        try:
            year = int(request.POST['year'])
            semester = request.POST['semester']
            course1 = request.POST['course1']
            course2 = request.POST['course2']
            courses = Course.objects.filter(name__in=[course1,course2])

            S = Semester.objects.create(year=year,semester=semester)
            S.course.add(*courses)
        except Exception as e:
            print(e)
            return HttpResponse('uncorrect')
        return HttpResponse("ok")



