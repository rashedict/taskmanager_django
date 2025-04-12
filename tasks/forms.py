from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Task

# Custom Login Form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

# Task Form to Add Tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']  # Define which fields you want to include in the form
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title',
                'class': 'title-field'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'checkbox-field'
            }),
        }