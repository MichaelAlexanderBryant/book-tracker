from django.urls import path

from .views import HomePageView, AuthorListView, GenreListView, PublicationListView

urlpatterns = [
    path("publications/", PublicationListView.as_view(), name="publications"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("", HomePageView, name="home")
]