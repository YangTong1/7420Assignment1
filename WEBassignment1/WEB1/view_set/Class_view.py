from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *

@login_required
@permission_required('WEB1.add_class',raise_exception=True)
def add_Class(request):
    if request.method == "GET":
        return render(request,'add_Class.html')
    elif request.method == "POST":
        number = int(request.POST['number'])
        course = request.POST['course']
        semester = request.POST['semester']
        lecturer = request.POST['lecturer']

        student = request.POST['student']
        stu = student.split(',')

        try:
            mycourse = Course.objects.get(name=course)
            mysemester = Semester.objects.get(semester=semester)
            mylecturer = Lecturer.objects.get(staff_id=lecturer)
            s = Student.objects.filter(student_id__in=stu)

            myclass = Class.objects.create(number=number,course=mycourse,semester=mysemester,lecturer=mylecturer)
            myclass.student.add(*s)
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')



@login_required
@permission_required('WEB1.view_class',raise_exception=True)
def select_class(request):
    myclass = Class.objects.all()
    return render(request,'select_class.html',{'myclass':myclass})


@login_required
@permission_required('WEB1.change_class',raise_exception=True)
def change_class(request):
    if request.method == 'GET':
        id = request.GET['cid']
        cla = Class.objects.get(id=id)
        lecturers = Lecturer.objects.all()
        courses = Course.objects.all()
        semesters = Semester.objects.all()

        mylectuer = cla.lecturer
        mycourse = cla.course
        mysemester = cla.semester
        return render(request,'change_class.html',{'lecturers':lecturers,'semesters':semesters,'courses':courses,'mylecturer':mylectuer,'mycourse':mycourse,'mysemester':mysemester,'cla':cla})

    elif request.method == 'POST':
        cid = request.POST['class_id']
        number = request.POST['number']
        coursetags = request.POST.getlist('ctags')
        lecturertags = request.POST.getlist('ltags')
        semestertags = request.POST.getlist('stags')
        if len(coursetags) > 1:
            return HttpResponse('course only choose one')
        c = Course.objects.get(id=coursetags[0])
        if len(lecturertags) > 1:
            return HttpResponse('lecturer only choose one')
        l = Lecturer.objects.get(staff_id=lecturertags[0])
        if len(semestertags) > 1:
            return HttpResponse('semester only choose one')
        s = Semester.objects.get(id=semestertags[0])
        try:
            cla = Class.objects.get(id=cid)
            cla.course = c
            cla.lecturer = l
            cla.semester = s
            cla.number = number
            cla.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')


@login_required
@permission_required('WEB1.delete_class',raise_exception=True)
def delete_class(request):
    if request.method == 'GET':
        getid = request.GET['did']
        try:
            C = Class.objects.get(id=getid)
            C.delete()
            return redirect('/select_class/')
        except Exception as e:
            print(e)
            return HttpResponse('error')