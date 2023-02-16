from django.urls import path

from .views import (HomePageView, GenreListView, PublicationListView, CopiesListView, AuthorCreateView, GenreCreateView,
                    PublicationCreateView, CopyCreateView)

urlpatterns = [
    path("newcopy/", CopyCreateView.as_view(), name="new_copy"),
    path("newpublication/", PublicationCreateView.as_view(), name="new_publication"),
    path("newgenre/", GenreCreateView.as_view(), name="new_genre"),
    path("newauthor/", AuthorCreateView.as_view(), name="new_author"),
    path("publications/", PublicationListView.as_view(), name="publications"),
    path("copies/", CopiesListView.as_view(), name="copies"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("", HomePageView, name="home")
]