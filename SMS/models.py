from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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


class TeacherManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        teacher = self.model(email=email, **extra_fields)
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Teacher(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, default='example@example.com')
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=128, default='temporary_password')
    admin = models.BooleanField(default=False)
    courses = models.ManyToManyField('Course', related_name='classes')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
