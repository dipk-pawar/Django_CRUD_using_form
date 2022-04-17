from django.core import validators
from django import forms
from .models import Employee

class EmployeeRegistration(forms.ModelForm):
 class Meta:
  model = Employee
  fields = ['name', 'email', 'salary', 'password']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'salary': forms.TextInput(attrs={'class':'form-control'}),
   'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
  }