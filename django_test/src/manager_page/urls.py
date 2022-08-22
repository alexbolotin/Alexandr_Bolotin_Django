from django.urls import path
from . import views

app_name = 'managers'

urlpatterns = [ 
    path('main-menu', views.MainPage.as_view(), name = "main-menu"),
    path('all-customers', views.AllCustomers.as_view(), name = "all-customers"),
    path('all-carts-by-status', views.AllCartsByStatus.as_view(), name = "all-carts-by-status"),
    path('all-carts-by-status-update', views.AllCartsByStatusUpdate.as_view(), name = "all-carts-by-status-update"),
    path('customer-choice', views.CustomerСhoice.as_view(), name = "customer-choice"),
    path('customer-profile', views.CustomerProfile.as_view(), name = "customer-profile"),
    path('all-customers-carts', views.CustomersCarts.as_view(), name = "all-customers-carts"),
    path('books-in-cart', views.BooksInCart.as_view(), name = "books-in-cart"),
    path('books-in-cart-update', views.BooksInCartUpdate.as_view(), name = "books-in-cart-update"),

]