from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    competencies = models.CharField(max_length=100)
    initial_date = models.DateField()
    final_date = models.DateField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    attendant_name = models.CharField(max_length=25)
    attendant_phone = models.CharField(max_length=25)
    group = models.CharField(max_length=100)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    admin = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course, related_name='classes')

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
