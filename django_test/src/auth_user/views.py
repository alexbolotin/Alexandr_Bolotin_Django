from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from django.shortcuts import render, redirect

from .forms import CustomUserForm
from django.views.generic import TemplateView,DetailView,ListView
from orders import models as order_model
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def def_next_page(value):
    previous = value.request.META.get('HTTP_REFERER')
    print(previous)
    find = ['/auth/','/order/','/orders/']
    for url in find:
        x = previous.lower().count(url)
        if x:
            break
    if x:
        next_page = "/"
    else:
        next_page = previous
    return next_page

class LoginUserView(auth_views.LoginView):
    template_name = "auth_user/login.html"

    def get_default_redirect_url(self):
        url = reverse_lazy("books:book-view-all")              
        return resolve_url(url)

class LogoutUserView(auth_views.LogoutView):
    template_name = "directory/home_page.html"

    def get_next_page(self):
        next_page = def_next_page(self)
        return next_page

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = request.POST.get("username")
            user = User.objects.get(username = user_name)
            my_group = Group.objects.get(name='Users') 
            user.groups.add(my_group)
            return redirect('auth:login')
    context = {'form': form}
    return render(request, 'auth_user/registration.html', context)


class UserPage(LoginRequiredMixin,TemplateView):
    template_name = "auth_user/user_page.html"
    model = order_model.Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        customer = self.request.user
        carts = order_model.Cart.objects.filter(customer = customer)
        context['carts'] = carts
        return context
    
class CartsList(LoginRequiredMixin,ListView):
    template_name = "auth_user/carts_view.html"
    model = order_model.Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        customer = self.request.user
        if customer != "AnonymousUser":
            carts = order_model.Cart.objects.filter(customer = self.request.user)
            context['carts'] = carts
        else:
            print('2',customer)
            context['carts'] = None
        return context


class CartView(LoginRequiredMixin,DetailView):
    template_name = "auth_user/cart_view.html"
    model = order_model.Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        session_id = self.object.session_id
        cart = order_model.Cart.objects.get(session_id = session_id)
        books = order_model.BookInCart.objects.filter(cart = cart)
        context['cart'] = cart
        context['books'] = books
        return context