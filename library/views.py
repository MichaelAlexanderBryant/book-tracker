from django.views.generic import ListView

from .models import Author, Genre, Publication

class HomeListView(ListView):
    model = Author
    template_name = "home.html"

class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"

class GenreListView(ListView):
    model = Genre
    template_name = "genre_list.html"

class PublicationListView(ListView):
    model = Publication
    template_name = "publication_list.html"