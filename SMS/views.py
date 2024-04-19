from django.shortcuts import render, redirect
from .models import Course, Student
from django.contrib import messages
from sms import send_sms

def home(request):
    return render(request, 'home.html')

def create_course(request):
    students = Student.objects.all()

    if request.method == 'POST':

        subject = request.POST.get('subject')
        competencies = request.POST.get('competencies')
        initial_date = request.POST.get('initial_date')
        final_date = request.POST.get('final_date')
        students_ids = request.POST.getlist('students')

        new_course = Course.objects.create(
            subject=subject,
            competencies=competencies,
            initial_date=initial_date,
            final_date=final_date
        )

        new_course.students.set(students_ids)

        new_course.save()

        messages.success(request, 'Curso creado satisfactoriamente.')
        return redirect('create_course')
    
    return render(request, 'create_course.html', {'students': students})

def show_course(request):
    courses = Course.objects.all()
    return render(request, 'show_course.html', {'courses': courses})

def create_student(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        group = request.POST.get('group')
        attendant_name = request.POST.get('attendant_name')
        attendant_phone = request.POST.get('attendant_phone')

        new_student = Student.objects.create(
            name=name,
            group=group,
            attendant_name=attendant_name,
            attendant_phone=attendant_phone
        )

        new_student.save()

        messages.success(request, 'Estudiante creado satisfactoriamente.')
        return redirect('create_student')
    
    return render(request, 'create_student.html')

def show_students(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.all()
    return render(request, 'show_students.html', {'students': students, 'course': course})

def generate_report(request, course_id, student_id):
    student = Student.objects.get(id=student_id)
    Course.objects.get(id=course_id)

    if request.method == 'POST':
        attended = request.POST.get('attended')
        observations = request.POST.get('observations')
        msg = ""
        status = send_sms()
    return render(request, 'generate_report.html')