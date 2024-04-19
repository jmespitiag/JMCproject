from django.shortcuts import render
from .models import Course, Student

def home(request):
    return render(request, 'home.html')

def create_course(request):
    students = Student.objects.all()
    return render(request, 'create_course.html', {'students': students})

def show_course(request):
    courses = Course.objects.all()
    return render(request, 'show_course.html', {'courses', courses})