from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Task
from .forms import CustomLoginForm, TaskForm

# Task list view for logged-in users
@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Login view to handle user login
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'registration/login.html', {'form': form})

# Logout view to log out the user
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

# Register view to handle user sign-up
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Home page view for logged-in users
@login_required
def home(request):
    return render(request, 'tasks/home.html')

# Task list view for logged-in users
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Only show tasks for the logged-in user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# New task creation view
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the logged-in user to the task
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task-list')  # Redirect to the task list page after adding the task
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})
