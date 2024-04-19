from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    attendant_name = models.CharField(max_length=25)
    attendant_phone = models.CharField(max_length=25)
    group = models.CharField(max_length=100)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    competencies = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    initial_date = models.DateField()
    final_date = models.DateField()