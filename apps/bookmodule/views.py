from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm


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

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
 
    return render(request, 'bookmodule/search.html')



def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains=' non ') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 10)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=20))
    context = {'books': books}
    return render(request, 'bookmodule/lab8_task1.html', context)

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    context = {'books': books}
    return render(request, 'bookmodule/lab8_task2.html', context)

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        (~Q(title__icontains='co') |
        ~Q(author__icontains='co'))
    )
    context = {'books': books}
    return render(request, 'bookmodule/lab8_task3.html', context)

def lab8_task4(request):
    books = Book.objects.all().order_by('title')  # ascending alphabetical order
    context = {'books': books}
    return render(request, 'bookmodule/lab8_task4.html', context)


def lab8_task5(request):
    stats = Book.objects.aggregate(
        num_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    context = {'stats': stats}
    return render(request, 'bookmodule/lab8_task5.html', context)

def listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        if title and author and price and edition:
            Book.objects.create(title=title, author=author, price=float(price), edition=int(edition))
            return redirect('books.listbooks')
        else:
            return render(request, 'bookmodule/addbook.html', {'error': 'All fields are required'})
    
    return render(request, 'bookmodule/addbook.html')


def editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        if title and author and price and edition:
            book.title = title
            book.author = author
            book.price = float(price)
            book.edition = int(edition)
            book.save()
            return redirect('books.listbooks')
        else:
            return render(request, 'bookmodule/editbook.html', {'book': book, 'error': 'All fields are required'})

    return render(request, 'bookmodule/editbook.html', {'book': book})



def deletebook(request,id):
    book = Book.objects.get(id = id)
    if request.method=='POST':
        book.delete()
        return redirect('books.listbooks')
    return render(request, "bookmodule/deletebook.html", {'book':book})


def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/part2_listbooks.html', {'books': books})


def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/part2_addbook.html', {'form': form})



def edit_book_part2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/part2_editbook.html', {'form': form, 'book': book})


def delete_book_part2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_part2')
    return render(request, 'bookmodule/part2_deletebook.html', {'book': book})