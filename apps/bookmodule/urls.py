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
]

