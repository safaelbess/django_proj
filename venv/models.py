from django.db import models



class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subject_name = models.ForeignKey('Subject')
    student_name = models.ForeignKey('Student')

    def __str__(self):
        return self.first_name 



class Subject(models.Model):
    sub_name = models.CharField(max_length=200)
    teacher_name = models.ForeignKey('Teacher')
    student_name = models.ForeignKey('Student')
    def __str__(self):
        return self.sub_name 
 

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    teacher_name = models.ForeignKey('Teacher')
    subject_name = models.ForeignKey('Subject')

    def __str__(self):
        return self.first_name 
    