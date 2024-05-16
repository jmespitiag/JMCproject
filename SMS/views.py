from django.shortcuts import render, redirect
from .models import Course, Student
from django.contrib import messages
from .sms import send_sms
from datetime import date

def home(request):
    return render(request, 'home.html')

def create_course(request):
    students = Student.objects.all()

    if request.method == 'POST':

        subject = request.POST.get('subject')
        competencies = request.POST.get('competencies')
        initial_date = request.POST.get('initial_date')
        final_date = request.POST.get('final_date')
        students_id = request.POST.getlist('students')
        print(students_id)

        new_course = Course.objects.create(
            subject=subject,
            competencies=competencies,
            initial_date=initial_date,
            final_date=final_date
        )

        for student_id in students_id:
            x = Student.objects.get(id=student_id)
            print(x)
            new_course.students.add(x)

        new_course.save()
        updated_course = Course.objects.get(pk=new_course.pk)
        print(updated_course.students.all())

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
    students = course.students.all()
    print(course)
    print("aa")
    print(course.students.exists())
    return render(request, 'show_students.html', {'students': students, 'course': course})

def generate_report(request, course_id, student_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    date_today = date.today()
    

    if request.method == 'POST':
        attended = request.POST.get('attended')
        observations = request.POST.get('observations')
        msg = f"JUAN MARÍA CÉSPEDES\n\n!Hola {student.attendant_name}!, le informamos que el/la estudiante {student.name} tuvo el día\nde hoy {date_today},una sesión de un curso remedial. Aquí hay alguna información importante:\n\nAsistió: {attended}\nMateria del curso: {course.subject}\n\nObservaciones del docente:{observations}\n\n ¡Gracias por su atención! Para más información recuerda asisitir a los miércoles en familia"     
        status = send_sms(student.attendant_phone, msg)
        messages.success(request, status)
        return redirect('generate_report', course_id=course_id, student_id=student_id)
    return render(request, 'generate_report.html')

def show_session(request, session_id):
    pass

def create_session(request):
    pass

def generate_report(request,session_id, student_id):
    pass