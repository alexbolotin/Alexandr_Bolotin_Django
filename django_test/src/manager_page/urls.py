from django.urls import path
from . import views

app_name = 'managers'

urlpatterns = [ 
    path('main-menu', views.MainPage.as_view(), name = "main-menu"),
    path('all-customers', views.AllCustomers.as_view(), name = "all-customers"),
    path('all-customers-carts', views.CustomersCarts.as_view(), name = "all-customers-carts"),
    path('books-in-cart', views.BooksInCart.as_view(), name = "books-in-cart"),
    path('books-in-cart-update', views.BooksInCartUpdate.as_view(), name = "books-in-cart-update"),


]