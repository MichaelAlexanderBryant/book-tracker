from django.urls import path

from .views import (HomePageView, GenreListView, AuthorListView, PublicationListView, CopiesListView, AuthorCreateView, GenreCreateView,
                    PublicationCreateView, CopyCreateView, PublicationDetailView, AuthorDetailView, GenreDetailView, CopiesDetailView,
                    PublicationUpdateView, AuthorUpdateView, GenreUpdateView, CopyUpdateView)

urlpatterns = [
    path("detailcopy/<int:pk>/update", CopyUpdateView.as_view(), name="update_copy"),
    path("detailgenre/<int:pk>/update", GenreUpdateView.as_view(), name="update_genre"),
    path("detailauthor/<int:pk>/update", AuthorUpdateView.as_view(), name="update_author"),
    path("detailpublication/<int:pk>/update", PublicationUpdateView.as_view(), name="update_publication"),
    path("detailcopy/<int:pk>/", CopiesDetailView.as_view(), name="detail_copy"),
    path("detailgenre/<int:pk>/", GenreDetailView.as_view(), name="detail_genre"),
    path("detailauthor/<int:pk>/", AuthorDetailView.as_view(), name="detail_author"),
    path("detailpublication/<int:pk>/", PublicationDetailView.as_view(), name="detail_publication"),
    path("newcopy/", CopyCreateView.as_view(), name="new_copy"),
    path("newpublication/", PublicationCreateView.as_view(), name="new_publication"),
    path("newgenre/", GenreCreateView.as_view(), name="new_genre"),
    path("newauthor/", AuthorCreateView.as_view(), name="new_author"),
    path("publications/", PublicationListView.as_view(), name="publications"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    path("copies/", CopiesListView.as_view(), name="copies"),
    path("genres/", GenreListView.as_view(), name="genres"),
    path("", HomePageView, name="home")
]