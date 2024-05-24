from django.shortcuts import render, redirect
from .models import Course, Student, Teacher, Session
from django.contrib import messages
from .sms import send_sms
from django.contrib.auth.decorators import login_required
from .forms import TeacherRegistrationForm
from datetime import date
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import TeacherLoginForm
from .decorators import admin_required
from django.db.models import Count



def admin_home(request):
    return render(request, 'admin_home.html')

@login_required
def user_home(request):
    return render(request, 'user_home.html')

@login_required
def home(request):
    if request.user.admin:
        return redirect('admin_home')
    else:
        return redirect('user_home')

@login_required
@admin_required
def create_course(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':

        subject = request.POST.get('subject')
        competencies = request.POST.get('competencies')
        initial_date = request.POST.get('initial_date')
        final_date = request.POST.get('final_date')
        students_id = request.POST.getlist('students')
        teacher_id = request.POST.get('teacher')
        teacher = Teacher.objects.get(id=teacher_id)
        print(students_id)

        new_course = Course.objects.create(
            subject=subject,
            competencies=competencies,
            initial_date=initial_date,
            final_date=final_date,
            teacher=teacher
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
    
    return render(request, 'create_course.html', {'students': students, 'teachers': teachers})

@login_required
@admin_required
def show_all_courses(request):
    courses = Course.objects.all()
    return render(request, 'show_all_courses.html', {'courses': courses})

@login_required
def show_my_courses(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'show_my_courses.html', {'courses': courses})

@login_required
@admin_required
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

@login_required
def show_students(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    print(course)
    print("aa")
    print(course.students.exists())
    return render(request, 'show_students.html', {'students': students, 'course': course})




@login_required
@admin_required
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.set_password(form.cleaned_data['password'])
            teacher.save()

            return redirect('home')
    else:
        form = TeacherRegistrationForm()
    
    return render(request, 'create_teacher.html', {'form': form})

@login_required
def show_session(request, session_id, last):
    session = Session.objects.get(id=session_id)
    students = session.students.all()
    reported_students = request.session.get('reported_students', None)
    
    if reported_students is None:
        reported_students = []
        request.session['reported_students'] = reported_students
        
    students_to_report = [student for student in students if student.id not in reported_students]

    return render(request, 'show_session.html', {'students': students_to_report, 'session_id': session.id, 'last': last})

@login_required
def create_session(request):
    last = 0
    if request.method == 'POST':

        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        if Session.objects.filter(course=course):
            last = 1
        students = course.students.all()
        teacher = request.user

        new_session = Session.objects.create(

            course = course,
            teacher = teacher

        )

        new_session.students.set(students)
        new_session.save()
        updated_session= Session.objects.get(pk=new_session.id)
        print(updated_session.students.all())

        return redirect('show_session',session_id=updated_session.id, last=last )
    


    else:
        
        courses = Course.objects.filter(teacher=request.user)

        # Usamos 'annotate()' para agregar un nuevo campo que cuenta el número de sesiones por curso
        courses_with_session_count = courses.annotate(session_count=Count('session'))

        # Filtramos esos cursos para obtener solo aquellos con menos de dos sesiones
        courses_with_less_than_two_sessions = courses_with_session_count.filter(session_count__lt=2)
        
        
        
    return render(request, 'create_session.html', {'courses':courses_with_less_than_two_sessions})

@login_required
def generate_report(request, session_id, student_id, last):
    student = Student.objects.get(id=student_id)
    session = Session.objects.get(id=session_id)
    course = session.course

    
    if request.method == 'POST':
        attended = request.POST.get('attended')
        observations = request.POST.get('observations')
        virtual_course = request.POST.get('virtual_course')
        if last == 1: 
            remedial_course = request.POST.get('remedial_course')
            msg = f"JUAN MARÍA CÉSPEDES\n\n!Hola {student.attendant_name}!, le informamos que el/la estudiante {student.name} tuvo el día\nde hoy {session.date},una sesión de un curso remedial. Aquí hay alguna información importante:\n\nAsistió: {attended}\n¿Realizó el curso virtual?: {virtual_course}\n¿Aprobó el curso remedial?: {remedial_course}\nMateria del curso: {course.subject}\n\nObservaciones del docente:{observations}\n\n ¡Gracias por su atención! Para más información recuerda asistir a los miércoles en familia"
        else:
            msg = f"JUAN MARÍA CÉSPEDES\n\n!Hola {student.attendant_name}!, le informamos que el/la estudiante {student.name} tuvo el día\nde hoy {session.date},una sesión de un curso remedial. Aquí hay alguna información importante:\n\nAsistió: {attended}\n¿Realizó el curso virtual?: {virtual_course}\n\nObservaciones del docente:{observations}\n\n ¡Gracias por su atención! Para más información recuerda asistir a los miércoles en familia"    


        status = send_sms(student.attendant_phone, msg)
        messages.success(request, status)

        reported_students = request.session.get('reported_students', [])
        reported_students.append(student.id)
        request.session['reported_students'] = reported_students
        
        messages.success(request, f'Alumno {student.name} reportado.')
        return redirect('show_session', session_id=session_id)

    else:
        return render(request, 'generate_report.html',{'student':student, 'last':last})


class login(LoginView):
    template_name = 'login.html'
    authentication_form = TeacherLoginForm

def custom_logout(request):
    logout(request)
    return redirect('login')

