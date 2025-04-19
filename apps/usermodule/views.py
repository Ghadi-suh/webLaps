from django.shortcuts import render
from .models import Address
from django.db.models import Count, Min
from .models import Student, Card, Department, Course, StudentLap9
from django.db import models


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