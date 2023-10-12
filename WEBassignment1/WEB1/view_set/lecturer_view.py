from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *
from django.core.files.storage import FileSystemStorage
import pandas as pd

@login_required
@permission_required('WEB1.add_lecturer',raise_exception=True)
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


@login_required
@permission_required('WEB1.view_lecturer',raise_exception=True)
def select_lecturer(request):
    if request.method == 'GET':
        l = Lecturer.objects.all()
        return render(request,'select_lecturer.html',{'mylecturer':l})

@login_required
@permission_required('WEB1.change_lecturer',raise_exception=True)
def change_lecturer(request):
    if request.method == 'GET':
        getid = request.GET['cid']
        l = Lecturer.objects.get(staff_id=getid)
        myuser = l.user
        users = User.objects.all()
        return render(request,'change_lecturer.html',{'l':l,'myuser':myuser,'users':users})

    elif request.method == 'POST':
        tags = request.POST.getlist('tags')
        if len(tags) > 1:
            return HttpResponse('one lecturer only match one user')
        print(f'当前tags： {tags}')
        staff_id = request.POST['lecturer_id']
        DOB = request.POST['DOB']
        try:
            L = Lecturer.objects.get(staff_id=staff_id)
            L.DOB = DOB

            myuser = User.objects.get(username=tags[0])
            L.user = myuser
            L.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')



@login_required
@permission_required('WEB1.delete_lecturer',raise_exception=True)
def delete_lecturer(request):
    if request.method == 'GET':
        getid = request.GET['did']

        try:
            l = Lecturer.objects.get(staff_id=getid)
            l.delete()
            return redirect('select_lecturer')
        except Exception as e:
            print(e)
            return HttpResponse('error')


@login_required
@permission_required('WEB1.change_student',raise_exception=True)
def upload_file(request):
    if request.method == 'GET':
        return render(request,'upload_file.html')
    elif request.method == 'POST' and request.FILES['stu_file']:
        stufile = request.FILES['stu_file']#获取前端上传文件
        fs = FileSystemStorage()
        file = fs.save(stufile.name,stufile)#上传的文件存在media

        data = pd.read_excel(stufile)
        data = pd.DataFrame(data, columns=["student_id","attend"])
        stu_id = data["student_id"].tolist()#python列表
        attend = data["attend"].tolist()
        for i in range(len(stu_id)):
            student = Student.objects.get(student_id=stu_id[i])
            student.attend = attend[i]
            student.save()
        return redirect('/select_student/')


@login_required
@permission_required('WEB1.change_student',raise_exception=True)
def change_attendance(request):
    if request.method == 'GET':
        getid = request.GET['stuid']
        stu = Student.objects.get(student_id=getid)
        return render(request,'change_attendance.html',{'stu':stu})
    elif request.method == 'POST':
        getid = request.POST['id']
        att = request.POST['attendance']
        try:
            stu = Student.objects.get(student_id=getid)
            stu.attend = att
            stu.save()
            return HttpResponse('ok')
        except Exception as e:
            print(e)
            return HttpResponse('error')

@login_required
@permission_required('AttSystem.view_lecturer', raise_exception=True)
def lecturer_class(request):
    if request.method == 'GET':
        classes = Class.objects.all()
        return render(request, 'lec_class.html', {"classes":classes})

@login_required
@permission_required('AttSystem.change_class', raise_exception=True)
def assign(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        cla = Class.objects.get(id=id)
        #查询出所有的lecturer、course、semester
        lecturers = Lecturer.objects.all()
        mylecturer = cla.lecturer
        locals().update()
        return render(request, 'assign.html',locals())
    elif request.method == 'POST':
        cid = request.POST.get("class_id")
        ltags = request.POST.getlist("ltags") #lecturer
        if (len(ltags))>1:
            return HttpResponse("error!")
        try:
            l = Lecturer.objects.get(staff_id=ltags[0])
            cla = Class.objects.get(id=cid)
            cla.lecturer = l
            cla.save()
            return HttpResponse("ok")
        except Exception as e:
            print(e)
            return HttpResponse("error")

