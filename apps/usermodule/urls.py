from django.urls import path
from . import views

urlpatterns = [
    path("lab8/task7/", views.lab8_task7, name="users.lab8_task7"),   
    path("lab9/task1/", views.lab9_task1, name="users.lab9_task1"),   
    path("lab9/task2/", views.lab9_task2, name="users.lab9_task2"),
    path("lab9/task3/", views.lab9_task3, name="users.lab9_task3"),
    path("lab9/task4/", views.lab9_task4, name="users.lab9_task4"),
]
