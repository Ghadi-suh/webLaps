from django.shortcuts import render
from .models import Address
from django.db.models import Count
from .models import Student


def lab8_task7(request):
    city_counts = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'usermodule/lab8_task7.html', {'city_counts': city_counts})