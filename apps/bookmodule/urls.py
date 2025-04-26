from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexx, name= "books.indexx"),
    path('index2/<int:val1>/', views.index2),
    path('index2/<str:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.viewbook"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path("html5/links/", views.html5_links, name="books.html5_links"),   
    path("html5/text/formatting", views.text_formatting, name="books.text_formatting"),
    path("html5/listing", views.list_elements, name="books.list_elements"),
    path("html5/table", views.table, name="books.table"),
    path("search/", views.search, name="books.search"),
    path("simple/query/", views.simple_query, name="books.simple_query"),
    path("complex/query/", views.lookup_query, name="books.lookup_query"),
    path("lab8/task1/", views.lab8_task1, name="books.lab8_task1"),
    path("lab8/task2/", views.lab8_task2, name="books.lab8_task2"),
    path("lab8/task3/", views.lab8_task3, name="books.lab8_task3"),
    path("lab8/task4/", views.lab8_task4, name="books.lab8_task4"), 
    path("lab8/task5/", views.lab8_task5, name="books.lab8_task5"),      
    path("lab9/part1/listbooks", views.listbooks, name="books.listbooks"),
    path("lab9/part1/addbook", views.addbook, name="books.addbook"),
    path("lab9/part1/editbook/<int:id>", views.editbook, name="books.editbook"),
    path("lab9/part1/deletebook/<int:id>", views.deletebook, name="books.deletebook"),
    path('lab9/part2/listbooks', views.list_books_part2, name='list_books_part2'),
    path('lab9/part2/addbook', views.add_book_part2, name='add_book_part2'),
    path('lab9/part2/editbook/<int:id>', views.edit_book_part2, name='edit_book_part2'),
    path('lab9/part2/deletebook/<int:id>', views.delete_book_part2, name='delete_book_part2'),

]

