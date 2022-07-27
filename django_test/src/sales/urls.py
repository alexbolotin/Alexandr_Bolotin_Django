from django.urls import path
from . import views

app_name = 'sales'


urlpatterns = [ 
    
    # path('sales_view/', views.SalesCards.as_view(), name = "sales-view"),
    path('sales_book_add/', views.SalesBookAdd.as_view(), name = "sales-book-add"),
    path('sales_author_add/', views.SalesAuthorAdd.as_view(), name = "sales-author-add"),
    
    path('sales_books_view/', views.SalesBooksView.as_view(), name = "sales-books-view"),
    path('sales_authors_view/', views.SalesAuthorsView.as_view(), name = "sales-authors-view"),

    path('sales_book_view/<int:pk>/', views.SalesBookView.as_view(), name = "sales-book-view"),
    path('sales_author_view/<int:pk>/', views.SalesAuthorView.as_view(), name = "sales-author-view"),

    path('sales_book_edit/<int:pk>/', views.SalesBookEdit.as_view(), name = "sales-book-edit"),
    path('sales_book_delete/<int:pk>/', views.SalesBookDelete.as_view(), name = "sales-book-delete"),

    path('sales_author_edit/<int:pk>/', views.SalesAuthorEdit.as_view(), name = "sales-author-edit"),
    path('sales_author_delete/<int:pk>/', views.SalesAuthorDelete.as_view(), name = "sales-author-delete"),
]

