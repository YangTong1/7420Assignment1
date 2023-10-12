from django.shortcuts import render,redirect,HttpResponse
from WEB1.models import *
from django.utils import timezone as datetime
from django.contrib.auth.decorators import login_required, permission_required



@login_required
@permission_required('WEB1.add_collegeday',raise_exception=True)
def add_collegeDay(request):
    if request.method == "GET":
        return render(request,'add_collegeDay.html')
    elif request.method == "POST":

        #myclass = request.POST['class']


       #C = Class.objects.get(id=myclass)

        try:
            mydate = request.POST['date']
            myclass = request.POST['class']
            #print(myclass)
            stuclass = myclass.split(',')
            #print(stuclass)
            C = Class.objects.filter(id__in=stuclass)
            if C:
                #print("C's value = ",C)
                CD = CollegeDay.objects.create(date=mydate)
                CD.stuclass.add(*C)
                return HttpResponse("correct")
            else:
                return HttpResponse('error')
        except Exception as e:
            print(e)
            return HttpResponse('error')
