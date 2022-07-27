from django.urls import path
from . import views

app_name = 'dirs'

urlpatterns = [ 
    path('', views.Homepage.as_view(), name = "home-page"),

    path('books_view/', views.BooksList.as_view(), name = "book-view-all"),
    path('book_view/<int:pk>/', views.BookView.as_view(), name = "book-view"),
    path('book_add/', views.BookAdd.as_view(), name = "book-add"),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name = "book-delete"),
    path('book_edit/<int:pk>/', views.BookEdit.as_view(), name = "book-edit"),
    
    path('authors_view/', views.AuthorsList.as_view(), name = "author-view-all"),
    path('author_view/<int:pk>/', views.AuthorView.as_view(), name = "author-view"),
    path('author_edit/<int:pk>/', views.AuthorEdit.as_view(), name = "author-edit"),
    path('author_delete/<int:pk>/', views.AuthorDelete.as_view(), name = "author-delete"),
    path('author_add/', views.AuthorAdd.as_view(), name = "author-add"),

    path('publishings_view/', views.PublishingsList.as_view(), name = "publishing-view-all"),
    path('publishing_view/<int:pk>/', views.PublishingView.as_view(), name = "publishing-view"),
    path('publishing_edit/<int:pk>/', views.PublishingEdit.as_view(), name = "publishing-edit"),
    path('publishing_delete/<int:pk>/', views.PublishingDelete.as_view(), name = "publishing-delete"),
    path('publishing_add/', views.PublishingAdd.as_view(), name = "publishing-add"),

    path('serieses_view/', views.SeriesList.as_view(), name = "series-view-all"),
    path('series_view/<int:pk>/', views.SeriesView.as_view(), name = "series-view"),
    path('series_edit/<int:pk>/', views.SeriesEdit.as_view(), name = "series-edit"),
    path('series_delete/<int:pk>/', views.SeriesDelete.as_view(), name = "series-delete"),
    path('series_add/', views.SeriesAdd.as_view(), name = "series-add"),

    path('genres_view/', views.GenresList.as_view(), name = "genres-view-all"),
    path('genre_view/<int:pk>/', views.GenreView.as_view(), name = "genre-view"),
    path('genre_edit/<int:pk>/', views.GenreEdit.as_view(), name = "genre-edit"),
    path('genre_delete/<int:pk>/', views.GenreDelete.as_view(), name = "genre-delete"),
    path('genre_add/', views.GenreAdd.as_view(), name = "genre-add"),

]