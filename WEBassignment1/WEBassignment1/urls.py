"""
URL configuration for WEBassignment1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WEB1 import views
from WEB1.view_set import stu_view,login_view,Class_view,collegeDay_view,lecturer_view,course_view,semester_view,user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view.longin_v,name='login'),
    path('logout/',login_view.logout_v,name='logout'),
    path('',views.index,name='index'),
    #path('add_course/',views.add_course,name='add_course'),
    #path('add_lecturer/',views.add_lecturer,name='add_lecturer'),
    #path('add_semester/',views.add_semester,name='add_semester'),
    path('add_student/',stu_view.add_student,name='add_student'),
    path('select_student/',stu_view.select_student,name='select_student'),
    path('change_student/',stu_view.change_student,name='change_student'),
    path('delete_student/',stu_view.delete_student,name='delete_student'),
    path('stu_class/',stu_view.stu_class,name='stu_class'),
    path('enroll/',stu_view.enroll,name='enroll'),
    path('add_Class/',Class_view.add_Class,name='add_Class'),
    path('select_class/',Class_view.select_class,name='select_class'),
    path('change_class/',Class_view.change_class,name='change_class'),
    path('delete_class/',Class_view.delete_class,name='delete_class'),
    path('add_collegeDay/',collegeDay_view.add_collegeDay,name='add_collegeDay'),
    path('add_lecturer/',lecturer_view.add_lecturer,name='add_lecturer'),
    path('select_lecturer/',lecturer_view.select_lecturer,name='select_lecturer'),
    path('change_lecturer/',lecturer_view.change_lecturer,name='change_lecturer'),
    path('delete_lecturer/',lecturer_view.delete_lecturer,name='delete_lecturer'),
    path('lecturer_class/',lecturer_view.lecturer_class,name='lecturer_class'),
    path('assgin/',lecturer_view.assign,name='assign'),
    path('add_course/',course_view.add_course,name='add_course'),
    path('add_semester/',semester_view.add_semester,name='add_semester'),
    path('add_user/',user_view.add_user,name='add_user'),
    path('select_user/',user_view.select_user,name='select_user'),
    path('change_user/',user_view.change_user,name='change_user'),
    path('delete_user/',user_view.delete_user,name='delete_user'),
    path('select_course/',course_view.select_course,name='select_course'),
    path('change_course/',course_view.change_course,name='change_course'),
    path('delete_course/',course_view.delete_course,name='delete_course'),
    path('select_semester/',semester_view.select_semester,name='select_semester'),
    path('change_semester/',semester_view.change_semester,name='change_semester'),
    path('delete_semester/',semester_view.delete_semester,name='delete_semester'),
    path('upload_file/',lecturer_view.upload_file,name='upload_file'),
    path('change_attendance/',lecturer_view.change_attendance,name='change_attendance'),
    path('send_email/',stu_view.send_email,name='send_email'),
    path('welcome/',login_view.welcome,name='welcome')
]
