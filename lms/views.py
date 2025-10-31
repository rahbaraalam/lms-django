# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Material
# from .forms import MaterialForm
# from accounts.models import User

# # Create your views here.

# @login_required
# def teacher_dashboard(request):
#     materials = Material.objects.filter(created_by=request.user)
#     if request.method == 'POST':
#         form = MaterialForm(request.POST, request.FILES)
#         if form.is_valid():
#             mat = form.save(commit=False)
#             mat.created_by = request.user
#             mat.save()
#             return redirect('teacher_dashboard')
#     else:
#         form = MaterialForm()
#     return render(request, 'lms/teacher_dashboard.html', {'materials': materials, 'form': form})

# @login_required
# def student_dashboard(request):
#     materials = Material.objects.all()
#     return render(request, 'lms/student_dashboard.html', {'materials': materials})

# @login_required
# def admin_dashboard(request):
#     teachers = User.objects.filter(role='teacher')
#     students = User.objects.filter(role='student')
#     return render(request, 'lms/admin_dashboard.html', {'teachers': teachers, 'students': students})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def is_student(user):
    return user.groups.filter(name='Student').exists()

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'dashboards/admin_dashboard.html')

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    return render(request, 'dashboards/teacher_dashboard.html')

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'dashboards/student_dashboard.html')
