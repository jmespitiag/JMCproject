from django.contrib import admin
from .models import Student, Course, Session, Teacher


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Teacher)