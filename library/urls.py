from django.urls import path

from .views import HomeListView, AuthorListView, GenreListView, PublicationListView

urlpatterns = [
    path("publications/", PublicationListView.as_view(), name="publications"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("", HomeListView.as_view(), name="home")
]