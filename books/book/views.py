from django.shortcuts import render

# Create your views here.
from .models import Genre, Book, Author


def get_all(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {'genres': genres, 'books': books, 'authors': authors}

    return render(request, 'book/catalog.html', context)


