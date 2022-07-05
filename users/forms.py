from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Professor, Estudante

class TeacherForm(UserCreationForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = Professor
        fields = ["username", "matricula", "email", "password1", "password2"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if Professor.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))
        return e


class EditTeacherForm(UserCreationForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = Professor
        fields = ["email"]



class StudentForm(UserCreationForm):
    email=forms.EmailField(max_length=30)

    class Meta:
        model = Estudante
        fields = ["username", "matricula", "turma", "email", "password1", "password2"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if student.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))    
        return e