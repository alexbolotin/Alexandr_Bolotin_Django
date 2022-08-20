from django.shortcuts import render
from django.views.generic import TemplateView,DeleteView,ListView
from orders.models import Cart, BookInCart
from books.models import Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

class MainPage(TemplateView):
    template_name = 'managers/mian_manager_page.html'
    

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = Book.objects.all()
        context['books'] = books   

        User = get_user_model()
        users = User.objects.all()
        context['users'] = users        
        return context

class AllCustomers(ListView):
    template_name = 'managers/all_customers.html'
    model = User

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users        
        return context

class CustomersCarts(ListView):
    template_name = 'managers/customers_carts.html'
    model = Cart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.GET)
        user = User.objects.get(username = self.request.GET['customer'])
        carts = Cart.objects.filter(customer = user.pk)
        context['carts'] = carts       
        return context

class BooksInCart(ListView):
    template_name = 'managers/books_in_cart.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.GET)
        session = self.request.GET['session']
        cart = Cart.objects.get(session_id = session)
        customer = cart.customer

        books = BookInCart.objects.filter(cart = cart)

        context['cart'] = cart
        context['books'] = books
        context['customer'] = customer
        context['status'] = cart.status
        context['session'] = session

        note = cart.notes.replace('#', ': ')
        notes_lines = []
        notes_lines = note.split('\n')
        context['notes_lines'] = notes_lines
    
        return context

class BooksInCartUpdate(TemplateView):
    template_name = 'managers/books_in_cart_update.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.POST)

        session = self.request.POST['session']
        status = self.request.POST['status_']
        cart = Cart.objects.get(session_id = session)
        customer = cart.customer
        cart.status = status
        cart.save()
        books = BookInCart.objects.filter(cart = cart)
        context['books'] = books       
        context['customer'] = customer 
        context['status'] = cart.status 
        context['session'] = session

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