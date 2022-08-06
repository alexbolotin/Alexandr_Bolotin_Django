from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [ 
    path('login', views.LoginUserView.as_view(), name = "login"),
    path('logout', views.LogoutUserView.as_view(), name = "logout"),
    path('registration', views.register_page, name = "registration"),

]