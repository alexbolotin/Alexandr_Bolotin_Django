from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [ 
    path('books_view/', views.BooksList.as_view(), name = "book-view-all"),
    path('book_view/<int:pk>/', views.BookView.as_view(), name = "book-view"),
    path('book_add/', views.BookAdd.as_view(), name = "book-add"),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name = "book-delete"),
    path('book_edit/<int:pk>/', views.BookEdit.as_view(), name = "book-edit"),

]