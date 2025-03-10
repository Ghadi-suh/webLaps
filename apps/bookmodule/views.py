from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 

def indexx(request): 
    return render(request, "bookmodule/indexx.html") 

def index2(request, val1 = 0):
    try:
        val1 = int(val1)  
        return HttpResponse("value1 = " + str(val1))
    except ValueError:
        return HttpResponse("error, expected val1 to be integer")

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)


def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
 
def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')

def list_elements(request):
    return render(request, 'bookmodule/list_elements.html')

def table(request):
    return render(request, 'bookmodule/table.html')
