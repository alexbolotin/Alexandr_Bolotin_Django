from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView
from django.shortcuts import render, redirect,resolve_url
from django.urls import reverse_lazy

from .forms import CustomUserForm
from orders import models as order_model

# Create your views here.

def def_next_page(value):
    previous = value.request.META.get('HTTP_REFERER')
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
            context['carts'] = None

        return context


class CartView(LoginRequiredMixin,TemplateView):
    template_name = "auth_user/cart_view.html"
    model = order_model.Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.GET)
        session_id = self.request.GET['session']
        cart = order_model.Cart.objects.get(session_id = session_id)
        books = order_model.BookInCart.objects.filter(cart = cart)
        context['cart'] = cart
        context['books'] = books
        context['session'] = session_id
        
        note = cart.notes.replace('#', ': ')
        notes_lines = []
        notes_lines = note.split('\n')
        context['notes_lines'] = notes_lines

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class UpdateCartView(LoginRequiredMixin,TemplateView):
    template_name = "auth_user/cart_view_update.html"
    model = order_model.Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        session_id = self.request.POST['session']
        cart = order_model.Cart.objects.get(session_id = session_id)
        books = order_model.BookInCart.objects.filter(cart = cart)
        context['cart'] = cart
        context['books'] = books
        
        new_note = self.request.POST['notes']
        note = cart.notes
        note += 'user ' + str(self.request.user) + '#' + str(new_note) + '\n'
        cart.notes = note
        cart.save()
        note = cart.notes.replace('#', ': ')
        notes_lines = []
        notes_lines = note.split('\n')
        context['notes_lines'] = notes_lines

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)