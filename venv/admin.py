from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)


class AdminTeacher(admin.ModelAdmin):
    list_display =('first_name','last_name','specialize')

admin.site.register(Teacher,AdminTeacher)    



class AdminStudent(admin.ModelAdmin):
    list_display=('first_name','last_name','student_clas')

admin.site.register(Student,AdminStudent)


class SubjectAdmin(admin.ModelAdmin):
    list_display= {' sub_name ','teacher_name'}