from django.views.generic import TemplateView,ListView
from orders.models import Cart, BookInCart
from books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect



# Create your views here.

def has_perm(value,groups_has_perm):
    user_groups = value   
    for group in groups_has_perm:
        for user_group in user_groups:
            if str(user_group) == str(group):
                perm = True
                return perm
            else:
                perm =  False
    return perm

class MainPage(LoginRequiredMixin,UserPassesTestMixin, TemplateView):
    template_name = 'managers/mian_manager_page.html'
    login_url = '/auth/login'
    
    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = Book.objects.all()
        context['books'] = books   

        User = get_user_model()
        users = User.objects.all()
        context['users'] = users  

        return context

class AllCustomers(LoginRequiredMixin,UserPassesTestMixin,ListView):
    template_name = 'managers/all_customers.html'
    model = User
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        User = get_user_model()
        users = User.objects.all()
        context['users'] = users        
        return context

class CustomerСhoice(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'managers/customer_choice.html'
    model = User
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.GET)
        context['customer'] = self.request.GET['customer']      

        return context

class CustomerProfile(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'managers/customer_profile.html'
    model = User
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def handle_no_permission(self):
        return redirect('auth:login')


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        username_old = self.request.POST['username_old']
        context['username_old'] = username_old
        
        user = User.objects.get(username = username_old)

        try:
            username = self.request.POST['username']
        except:
            username = user.username

        try:
            first_name = self.request.POST['first_name']
        except:
            first_name = user.first_name
        
        try:
            last_name = self.request.POST['last_name']
        except:
            last_name = user.last_name

        try:
            email = self.request.POST['email']
        except:
            email = user.email

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        context['User_name'] = user.username
        context['First_name'] = user.first_name
        context['Last_name'] = user.last_name
        context['Email'] = user.email

    
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class CustomersCarts(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'managers/customers_carts.html'
    model = Cart
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        user = User.objects.get(username = self.request.POST['customer'])
        carts = Cart.objects.filter(customer = user.pk)
        context['carts'] = carts       
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class BooksInCart(LoginRequiredMixin,UserPassesTestMixin,ListView):
    template_name = 'managers/books_in_cart.html'
    model = BookInCart
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

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

class BooksInCartUpdate(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'managers/books_in_cart_update.html'
    model = BookInCart
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)

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

class AllCartsByStatus(LoginRequiredMixin,UserPassesTestMixin,ListView):
    template_name = 'managers/all_carts_by_status.html'
    model = Cart
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)  

        carts = Cart.objects.all()
        context['carts'] = carts

        return context

class AllCartsByStatusUpdate(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'managers/all_carts_by_status_update.html'
    model = Cart
    login_url = '/auth/login'

    def test_func(self):
        groups_has_perm = ['Managers','Super_managers','Admin']
        perm = has_perm(self.request.user.groups.all(),groups_has_perm)
        return perm

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)  
        status = self.request.POST['status']
        context['status'] = status

        if status != "All":
            carts = Cart.objects.filter(status = status)
        else:
            carts = Cart.objects.all()
        
        context['carts'] = carts

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)