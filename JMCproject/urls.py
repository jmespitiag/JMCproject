"""
URL configuration for JMCproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SMS import views as SMS
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('home/admin', SMS.admin_home, name='admin_home'),

    path('', SMS.home, name='home'),
    path('login/', SMS.login.as_view(), name='login'),
    path('logout/', SMS.custom_logout, name='logout'),
    

    path('courses/create', SMS.create_course, name='create_course'),
    path('courses/show/all', SMS.show_all_courses, name='show_all_courses'),
    path('courses/show/mine', SMS.show_my_courses, name='show_my_courses'),

    path('create_student/', SMS.create_student, name='create_student'),
    path('student/show/<int:course_id>', SMS.show_students, name='show_students'),

    path('teacher/create', SMS.create_teacher, name='create_teacher'),
    path('teacher/home', SMS.user_home, name='user_home'),

    path('session/<int:session_id>/<int:last>', SMS.show_session, name='show_session'),
    path('session/create', SMS.create_session, name='create_session'),
    path('session/<int:session_id>/<int:last>/<int:student_id>', SMS.generate_report, name='generate_report'),    
]
