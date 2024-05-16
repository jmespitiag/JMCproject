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

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('', SMS.home, name='home'), 

    path('course/create', SMS.create_course, name='create_course'),
    path('course/show', SMS.show_course, name='show_course'),

    path('student/create', SMS.create_student, name='create_student'),
    
    path('student/show/<int:course_id>', SMS.show_students, name='show_students'),

    path('course/session/<id:session_id>/', SMS.show_session, name='show_session'),
    path('course/session/create', SMS.create_session, name='create_session'),
    path('course/session/<id:session_id>/<id:student_id>', SMS.generate_report, name='generate_report'),    
]
