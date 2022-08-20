from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [ 
    path('login', views.LoginUserView.as_view(), name = "login"),
    path('logout', views.LogoutUserView.as_view(), name = "logout"),
    path('registration', views.register_page, name = "registration"),
    path('user-page', views.UserPage.as_view(), name = "user-page"),
    path('carts-view/', views.CartsList.as_view(), name = "carts-view"),
    path('cart_view/<int:pk>/', views.CartView.as_view(), name = "cart-view"),
    path('cart_view_update/<int:pk>/', views.UpdateCartView.as_view(), name = "cart-view-update"),

]