from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Address,  Student, Card, Department, Course, StudentLap9, Address2,  Student2, Photo
from django.db.models import Count, Min
from .forms import StudentForm, Student2Form
from .forms import PhotoForm


def lab8_task7(request):
    city_counts = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'usermodule/lab8_task7.html', {'city_counts': city_counts})

def lab9_task1(request):
    departments = Department.objects.all().annotate(student_count=models.Count('students'))
    return render(request, 'usermodule/lab9_task1.html', {'departments': departments})


def lab9_task2(request):
    courses = Course.objects.all().annotate(student_count=Count('students'))
    return render(request, 'usermodule/lab9_task2.html', {'courses': courses})

def lab9_task3(request):
    oldest_ids = StudentLap9.objects.values('department').annotate(oldest_id=Min('id'))
    oldest_id_list = [entry['oldest_id'] for entry in oldest_ids]
    oldest_students = StudentLap9.objects.filter(id__in=oldest_id_list).select_related('department')

    result = []
    for student in oldest_students:
        result.append({
            'department': student.department.name,
            'student': student.name,
            'student_id': student.id
        })
    return render(request, 'usermodule/lab9_task3.html', {'students': result})

def lab9_task4(request):
    departments = (
        Department.objects
        .annotate(student_count=Count('students'))  
        .filter(student_count__gt=2)
        .order_by('-student_count')
    )

    return render(request, 'usermodule/lab9_task4.html', {'departments': departments})    


    
# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'usermodule/student_list.html', {'students': students})

# Add a student
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'usermodule/student_form.html', {'form': form})

# Update a student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/student_form.html', {'form': form})

# Delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'usermodule/student_delete.html', {'student': student})



def students2_list(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/students2_list.html', {'students': students})


def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('students2_list')  # adjust to your URL name
    else:
        form = Student2Form()
    return render(request, 'usermodule/student2_form.html', {'form': form})



def update_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'usermodule/student2_form.html', {'form': form})



def delete_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students2_list')
    return render(request, 'usermodule/student2_delete.html', {'student': student})



def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_photos')  # or any page you want
    else:
        form = PhotoForm()
    return render(request, 'usermodule/upload_photo.html', {'form': form})


def list_photos(request):
    photos = Photo.objects.all()
    return render(request, 'usermodule/photo_list.html', {'photos': photos})
