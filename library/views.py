from django.views.generic import ListView
from django.shortcuts import render

from .models import Author, Book, Genre, Publication

def HomePageView(request):
    publication_count = Publication.objects.count()
    copies_count = Book.objects.count()
    copies_available_count = Book.objects.filter(status="available").count()
    author_count = Author.objects.count()
    genre_count = Genre.objects.count()
    context = {
        'publications': publication_count,
        'copies': copies_count,
        'copies_available': copies_available_count,
        'authors': author_count,
        'genres': genre_count 
    }
    template_name = "home.html"
    return render(request, template_name, context)

class PublicationListView(ListView):
    model = Publication
    template_name = "publication_list.html"

class GenreListView(ListView):
    model = Genre
    template_name = "genre_list.html"

class CopiesListView(ListView):
    model = Book
    template_name = "copy_list.html"



