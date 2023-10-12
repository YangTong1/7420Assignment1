from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telephone = models.CharField(max_length=33,blank=True)
    address = models.CharField(max_length=50)

class Lecturer(models.Model):
    staff_id = models.AutoField(primary_key=True)
    DOB = models.DateTimeField()
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=33)
    name = models.CharField(max_length=33)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    student = models.ManyToManyField("Student",related_name="student")
    course = models.ForeignKey("Course",on_delete=models.SET_NULL,null=True)
    lecturer = models.ForeignKey("Lecturer",on_delete=models.SET_NULL,null=True)
    semester = models.ForeignKey("Semester",on_delete=models.SET_NULL,null=True)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    DOB = models.DateTimeField()
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    attend = models.FloatField(null=True)
    course = models.ManyToManyField(Course)
    myclass = models.ManyToManyField("Class",related_name="myclass")



class CollegeDay(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    stuclass = models.ManyToManyField(Class)


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    semester = models.CharField(max_length=33)
    course = models.ManyToManyField(Course)
