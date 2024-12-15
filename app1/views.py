from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Author

def home(request):
    return render(request, 'app1/home.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'app1/list_books.html', {'books': books})

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'app1/book_details.html', {'book': book})

def add_books(request):
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.k. Rowling")

    Book.objects.create(title="1984",author=author1)
    Book.objects.create(title="Animal Farm",author=author1)
    Book.objects.create(title="Harry potter and the philospher's stone",author=author2)
    Book.objects.create(title="Harry potter and the chamber of Secrets",author=author2)

    return render (request,'home.html',{'message':'Books and authors added successfully!'})



