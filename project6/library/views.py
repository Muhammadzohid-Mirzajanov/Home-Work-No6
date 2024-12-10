from django.shortcuts import render,get_list_or_404
from .models import *

def index(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request,'library/html', {'categories':categories,'books':books})

def category_books(request, category_id):
    category = get_list_or_404(Category,id=category_id)
    books = Book.objects.filter(category=category)
    return render(request,'library/category_books.html', {'category': category, 'books':books})

def book_detail(request):
    book = get_list_or_404(Book,id=book_id)
    return render(request, 'library/book_detail.html', {'book':book})
