# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'accounts/home.html')

def register_view(request):
     if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False)
             # optionally, superusers are created via manage.py createsuperuser
             user.save()
             login(request, user)
             return redirect_role_dashboard(user)
     else:
         form = UserRegisterForm()
     return render(request, 'accounts/register.html', {'form': form})

def redirect_role_dashboard(user):
     if user.role == 'admin':
         return redirect('admin_dashboard')
     elif user.role == 'teacher':
         return redirect('teacher_dashboard')
     else:
         return redirect('student_dashboard')

 # Decorators to restrict access by role
def role_required(role):
     def decorator(view_func):
         @login_required
         def _wrapped(request, *args, **kwargs):
             if request.user.role != role:
                 return render(request, 'accounts/forbidden.html', status=403)
             return view_func(request, *args, **kwargs)
         return _wrapped
     return decorator

@role_required(User.ROLE_ADMIN)
def admin_dashboard(request):
     users = User.objects.all()
     teachers = User.objects.filter(role=User.ROLE_TEACHER).count()
     students = User.objects.filter(role=User.ROLE_STUDENT).count()
     return render(request, 'accounts/admin_dashboard.html', {'users': users, 'teachers': teachers, 'students': students})

@role_required(User.ROLE_TEACHER)
def teacher_dashboard(request):
     # Simple placeholder data
     students = User.objects.filter(role=User.ROLE_STUDENT)
     return render(request, 'accounts/teacher_dashboard.html', {'students': students})

@role_required(User.ROLE_STUDENT)
def student_dashboard(request):
     # Placeholder: enrolled courses or materials
     sample_materials = [
         {'title': 'Math Worksheet 1', 'description': 'Basic addition practice'},
         {'title': 'Science: Plants', 'description': 'Short notes on plant life'}
     ]
     return render(request, 'accounts/student_dashboard.html', {'materials': sample_materials})


def logout_view(request):
     logout(request)
     return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
