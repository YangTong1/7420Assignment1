from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *

@login_required
@permission_required('WEB1.add_course',raise_exception=True)
def add_course(request):
    if request.method == "GET":
        return render(request,"add_course.html")
    elif request.method == "POST":
        course_code = request.POST['course_code']
        course_name = request.POST['course_name']

        Course.objects.create(code=course_code,name=course_name)

        return HttpResponse('ok')

@login_required
@permission_required('WEB1.view_course',raise_exception=True)#要和admin里面权限对应
def select_course(request):
    if request.method == 'GET':
        mycourse = Course.objects.all()
        return render(request,'select_course.html',{'mycourse':mycourse})

@login_required
@permission_required('WEB1.change_course',raise_exception=True)
def change_course(request):
    if request.method == 'GET':
        getid = request.GET.get('id')
        c = Course.objects.get(id=getid)
        print(f'ID是:  :{c}')
        return render(request,'change_course.html',{"c":c})
    elif request.method == "POST":
        course_id = request.POST['course_id']
        course_code = request.POST['course_code']
        course_name = request.POST['course_name']

        try:
            c = Course.objects.get(id=course_id)
            c.name = course_name
            c.code = course_code
            c.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')



@login_required
@permission_required('WEB1.delete_course',raise_exception=True)
def delete_course(request):
    if request.method == 'GET':
        getid = request.GET['did']
        try:
            c = Course.objects.get(id=getid)
            c.delete()
            return redirect('/select_course/')
        except Exception as e:
            print(e)
            return HttpResponse('error')
