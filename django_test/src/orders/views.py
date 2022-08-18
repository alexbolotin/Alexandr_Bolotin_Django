from decimal import Decimal
from django.views.generic import TemplateView,DeleteView
from .models import Cart, BookInCart
from books.models import Book
from decimal import Decimal
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

def sale_for_groups(total_price,groups):
    
    if not groups:
        decimal = " no sale for unregistered user"
    else:
        for group in groups:
                if str(group) == "Admin":
                    total_price -= Decimal(0.2)*total_price
                    decimal = "-20 %"
                elif str(group) == "Users":
                    total_price -= Decimal(0.05)*total_price
                    decimal = "-5 %"
                elif str(group) == "Managers":
                    total_price -= Decimal(0.06)*total_price
                    decimal = "-6 %"
                elif str(group) == "Super_managers":
                    total_price -= Decimal(0.07)*total_price
                    decimal = "-7 %"
    return [total_price, decimal]


class AddToCart(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        book_id = self.request.POST['book_id']
        quantity = Decimal(self.request.POST['quantity'])
        cart_id = self.request.session.get("cart")
# who is customer:
        if self.request.user.is_anonymous:
            customer = None
        else:
            customer = self.request.user
# get or create a cart
        if customer:  # customer = True
            try: # get old cart
                carts = Cart.objects.filter(Q(customer = customer) & Q(status = "Start"))
                cart = carts.first()
                cart.status
            except:# create new cart
                cart = Cart.objects.create(
                            customer = customer,
                        )
                cart.session_id = cart.pk
                cart.save()
        else:  # customer = Anonymous
# new user without id in session
            if not cart_id: 
                cart = Cart.objects.create(
                        customer = customer,
                )
                cart.session_id = cart.pk
                cart.save()
# new user with id in session
            else:
                cart = Cart.objects.get(session_id = self.request.session['cart'])

# add a book to the cart
        book = Book.objects.get(pk = book_id)
        
        price = Decimal(Book.objects.get(pk = book_id).price) * quantity
        book_in_cart, created = BookInCart.objects.get_or_create(
            cart = cart,
            book = book,
            defaults={
                'quantity': quantity,
                'price': price
            }
        )
        if not created:
            if (book_in_cart.quantity+quantity) > book.quantity:
                book_in_cart.quantity = book.quantity
            else:
                book_in_cart.quantity += quantity
            book_in_cart.price = book_in_cart.quantity * price
            book_in_cart.save()

        context['request'] = self.request.POST
        context['session'] = cart.session_id
        context['cart'] = cart
        context['customer'] = cart.customer    
        context['book_in_cart'] = book_in_cart
    
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class BooksInCartList(TemplateView):
    template_name = 'orders/books_in_cart.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print('post',self.request.POST)
        
        customer = self.request.user
        carts = Cart.objects.filter(Q(customer = customer) & Q(status = "Start"))
        cart = carts.first()
        books = BookInCart.objects.filter(cart = cart)

        context['cart'] = cart
        context['session'] = cart.session_id
        context['books'] = books
        
        total_price = Decimal(0)
        for book in books:
            total_price += book.price
        context['total_price'] = total_price
        
        groups = self.request.user.groups.all()
        decimal = ""
        decimal = sale_for_groups(total_price,groups)[1]
        total_price_sale = sale_for_groups(total_price,groups)[0]
        context['total_price_sale'] = round(total_price_sale,2)
        context['decimal'] = decimal

        return context
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class DeleteFromCart(DeleteView):
    template_name = 'orders/delete_from_cart.html'
    model = BookInCart
    success_url = reverse_lazy("orders:books_list")

class OrderUpdateView(TemplateView):
    template_name = 'orders/books_in_cart.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        querydict = self.request.POST.copy()
        querydict.pop('csrfmiddlewaretoken')
        querydict.pop('session')
        session_id = self.request.POST['session']
        context['session'] = session_id

        total_price = 0
        for key in querydict.keys():
            book_in_cart_upd = BookInCart.objects.get(pk = int(key.split('/\\')[1]))
            book_in_cart_upd.quantity = int(self.request.POST.get(key))
            book_in_cart_upd.price = book_in_cart_upd.book.price * book_in_cart_upd.quantity
            book_in_cart_upd.save()
            total_price += book_in_cart_upd.price        

        context['total_price'] = total_price
        cart = Cart.objects.get(session_id = session_id)
        books = BookInCart.objects.filter(cart = cart)
        context['books'] = books

        groups = self.request.user.groups.all()
        decimal = sale_for_groups(total_price,groups)[1]
        context['decimal'] = decimal

        total_price_sale = sale_for_groups(total_price,groups)[0]
        context['total_price_sale'] = round(total_price_sale,2)
        context['session'] = cart.session_id
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)


class OrderConfirm(TemplateView):
    template_name = 'orders/order_confirm.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)
        
        session = self.request.POST['session']
        total_price = self.request.POST['total_price']
        cart = Cart.objects.get(session_id = session)
        context['cart'] = cart
        books = BookInCart.objects.filter(cart = cart)
        context['books'] = books
        context['total_price'] = total_price
        context['session'] = cart.session_id

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

    
class OrderStatus(TemplateView):
    template_name = 'orders/order_status.html'
    model = BookInCart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request.POST)

        session = self.request.POST['session']
        context['session'] = session

        carts = Cart.objects.all()
        context['carts'] = carts

        status = self.request.POST['status']
        if status == "Start":
            status = "Request"
        cart = Cart.objects.get(session_id = session)
        cart.status = status
        cart.save()
        context['status'] = status

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

class ChangeStatus(TemplateView):
    template_name = 'orders/order_status_update.html'
    model = Cart

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        session = self.request.POST['session']

        cart = Cart.objects.get(session_id = session)
        try:
            status = self.request.POST['status_']
            cart.status = status
            cart.save()
        except:
            pass

        context['status'] = cart.status
        if status == "Cancel":
            cart.status = "Close"
            cart.save()

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

