from django import forms
from .models import Teacher
from django.contrib.auth.forms import AuthenticationForm

class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Teacher
        fields = ['email', 'name', 'password', 'password_confirm', 'admin']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match.')

        return cleaned_data

class TeacherLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo Electrónico', max_length=254)


    