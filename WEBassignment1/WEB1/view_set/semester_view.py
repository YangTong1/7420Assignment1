from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *


@login_required
@permission_required('WEB1.add_semester',raise_exception=True)
def add_semester(request):
    if request.method == "GET":
        return render(request,'add_semester.html')
    elif request.method == "POST":
        try:
            year = int(request.POST['year'])
            semester = request.POST['semester']
            course = request.POST['course']
            C = course.split(',')
            courses = Course.objects.filter(name__in=C)

            S = Semester.objects.create(year=year,semester=semester)
            S.course.add(*courses)
        except Exception as e:
            print(e)
            return HttpResponse('uncorrect')
        return HttpResponse("ok")

@login_required
@permission_required('WEB1.view_semester',raise_exception=True)

def select_semester(request):
    if request.method == 'GET':
        clist = [] #存储各个学期课程
        mysemester = Semester.objects.all()
        #mysemester[0].course.all()#多对多关系必须加all
        for s in mysemester:
            #s.course.all()
            clist.append(s.course.all())
            #print(f'id是{s.course.all()}')
            print(clist)
        return render(request,'select_semester.html',{'mysemester':mysemester})



@login_required
@permission_required('WEB1.chage_semester',raise_exception=True)
def change_semester(request):
    if request.method == 'GET':
        id = request.GET['id']
        s = Semester.objects.get(id=id)
        c = s.course.all()
        courses = Course.objects.all()
        print(f'学期课程:{c}')
        print(f'所有课程:{courses}')
        check_id = []
        for x in c:
            check_id.append(x.id)
        return render(request,'change_semester.html',{'s':s,'courses':courses,'check_id':check_id})
    elif request.method == 'POST':
        tags = request.POST.getlist('tags')
        semester_id = request.POST.get('semester_id')
        year = request.POST.get('year')
        semester = request.POST['semester']
        clist = [] #用一个列表，存储change后的学期课程
        print(f'checkbox:{tags}')#查id
        for cid in tags:
            c = Course.objects.get(id=cid)#查询checked课程
            clist.append(c)
        print(clist)
        s = Semester.objects.get(id=semester_id)
        s.year = year
        s.semester = semester
        s.course.set(tags)#tags里面是课程ID
        s.save()
        return HttpResponse('ok')



@login_required
@permission_required('WEB1.delete_semester',raise_exception=True)
def delete_semester(request):
    if request.method == 'GET':
        getid = request.GET['did']
        try:
            s = Semester.objects.get(id=getid)
            s.delete()
            return redirect('select_semester')
        except Exception as e:
            print(e)
            return HttpResponse('error')
