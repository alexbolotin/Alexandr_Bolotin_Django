from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [ 
    path('add-to-cart', views.AddToCart.as_view(), name = "add-to-cart"),
    path('books_list', views.BooksInCartList.as_view(), name = "books_list"),
    path('delete_from_cart/<int:pk>', views.DeleteFromCart.as_view(), name = "delete_from_cart"),
    path('update-carts', views.OrderUpdateView.as_view(), name = "update-carts"),
    path('order-confirm', views.OrderConfirm.as_view(), name = "order-confirm"),
    path('order-status', views.OrderStatus.as_view(), name = "order-status"),
    path('order-status-update', views.ChangeStatus.as_view(), name = "order-status-update"),


]