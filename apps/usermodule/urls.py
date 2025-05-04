from django.urls import path
from . import views



urlpatterns = [
    path("lab8/task7/", views.lab8_task7, name="users.lab8_task7"),   
    path("lab9/task1/", views.lab9_task1, name="users.lab9_task1"),   
    path("lab9/task2/", views.lab9_task2, name="users.lab9_task2"),
    path("lab9/task3/", views.lab9_task3, name="users.lab9_task3"),
    path("lab9/task4/", views.lab9_task4, name="users.lab9_task4"),
    path('lab11/students/', views.student_list, name='student_list'),
    path('lab11/students/add/', views.student_add, name='student_add'),
    path('lab11/students/<int:pk>/update/', views.student_update, name='student_update'),
    path('lab11/students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('lab11/students2/', views.students2_list, name='students2_list'),
    path('lab11/students2/add/', views.add_student2, name='add_student2'),
    path('lab11/students2/update/<int:student_id>/', views.update_student2, name='update_student2'),
    path('lab11/students2/delete/<int:student_id>/', views.delete_student2, name='delete_student2'),
    path('lab11/photos/', views.list_photos, name='list_photos'),
    path('lab11/photos/add/', views.upload_photo, name='upload_photo'),
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logout_view, name='logout'),
] 


