from django.urls import path

from .views import HomePageView, GenreListView, PublicationListView, CopiesListView

urlpatterns = [
    path("publications/", PublicationListView.as_view(), name="publications"),
    path("copies/", CopiesListView.as_view(), name="copies"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("", HomePageView, name="home")
]