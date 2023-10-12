from django.contrib import admin
from django.contrib.auth.models import User

from WEB1.models import Student,Semester,Course,Class,CollegeDay,Lecturer,UserProfile
# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = UserProfile
    #Inline和ModelAdmin类的作用在于，可以在ModelA（user）页面上编辑ModelB（UserProfile）表的字段。
    #A和B存在外键关系即可

class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(CollegeDay)
admin.site.register(Lecturer)