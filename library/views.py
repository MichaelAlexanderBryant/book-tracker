from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render

from .models import Author, Book, Genre, Publication

# Homepage
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

# List views
class PublicationListView(ListView):
    model = Publication
    template_name = "publication_list.html"

class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"

class GenreListView(ListView):
    model = Genre
    template_name = "genre_list.html"

class CopiesListView(ListView):
    model = Book
    template_name = "copy_list.html"

# Create views
class AuthorCreateView(CreateView):
    model = Author
    template_name = "author_new.html"
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]

class GenreCreateView(CreateView):
    model = Genre
    template_name = "genre_new.html"
    fields = ["genre"]

class PublicationCreateView(CreateView):
    model = Publication
    template_name = "publication_new.html"
    fields = ["title", "author", "summary", "isbn", "genre"]

class CopyCreateView(CreateView):
    model = Book
    template_name = "copy_new.html"
    fields = ["book", "imprint", "status"]

# Detail views
class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publication_detail.html"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"

class GenreDetailView(DetailView):
    model = Genre
    template_name = "genre_detail.html"

class CopiesDetailView(DetailView):
    model = Book
    template_name = "copy_detail.html"

# Update views
class AuthorUpdateView(UpdateView):
    model = Author
    template_name = "author_update.html"
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]

class GenreUpdateView(UpdateView):
    model = Genre
    template_name = "genre_update.html"
    fields = ["genre"]

class PublicationUpdateView(UpdateView):
    model = Publication
    template_name = "publication_update.html"
    fields = ["title", "author", "summary", "isbn", "genre"]

class CopyUpdateView(UpdateView):
    model = Book
    template_name = "copy_update.html"
    fields = ["book", "imprint", "status"]