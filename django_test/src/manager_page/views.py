from django.shortcuts import render
from django.views.generic import TemplateView,DeleteView,ListView
from orders.models import Cart, BookInCart
from books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'managers/mian_manager_page.html'
    login_url = '/auth/login'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = Book.objects.all()
        context['books'] = books   

        User = get_user_model()
        users = User.objects.all()
        context['users'] = users        
        return context

class AllCustomers(LoginRequiredMixin,ListView):
    template_name = 'managers/all_customers.html'
    model = User
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users        
        return context

class CustomersCarts(LoginRequiredMixin,ListView):
    template_name = 'managers/customers_carts.html'
    model = Cart
    login_url = '/auth/login'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.GET)
        user = User.objects.get(username = self.request.GET['customer'])
        carts = Cart.objects.filter(customer = user.pk)
        context['carts'] = carts       
        return context

class BooksInCart(LoginRequiredMixin,ListView):
    template_name = 'managers/books_in_cart.html'
    model = BookInCart
    login_url = '/auth/login'

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

        if cart.notes:
            note = cart.notes.replace('#', ': ')
        else:
            note = "let's start chat? Say something\n"
        
        notes_lines = []
        notes_lines = note.split('\n')
        context['notes_lines'] = notes_lines
    
        return context

class BooksInCartUpdate(LoginRequiredMixin,TemplateView):
    template_name = 'managers/books_in_cart_update.html'
    model = BookInCart
    login_url = '/auth/login'

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
        print(note)
        if cart.notes:
            note = cart.notes.replace('#', ': ')
        else:
            note = "let's start chat? Say something\n" 
        note += 'manager ' + str(self.request.user) + '#' + str(new_note) + '\n'
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


class AllCartsByStatus(LoginRequiredMixin,ListView):
    template_name = 'managers/all_carts_by_status.html'
    model = Cart
    login_url = '/auth/login'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.POST)  

        carts = Cart.objects.all()
        context['carts'] = carts

        return context

class AllCartsByStatusUpdate(LoginRequiredMixin,TemplateView):
    template_name = 'managers/all_carts_by_status_update.html'
    model = Cart
    login_url = '/auth/login'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.POST)  
        status = self.request.POST['status']
        context['status'] = status

        print(status)

        carts = Cart.objects.filter(status = status)
        print(carts)
        context['carts'] = carts

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)