from django.views.generic import TemplateView,ListView
from .models import Cart, BookInCart
from books.models import Book

# Create your views here.

class AddToCart(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        book_id = self.request.POST['book_id']
        quantity = int(self.request.POST['quantity'])
        cart_id = self.request.session.get("cart")
        print(self.request.POST)
        # print(self.request.session.items())
        
        # who is customer:
        if self.request.user.is_anonymous:
            customer = None
        else:
            customer = self.request.user

        # get or create a cart
        if customer:  # customer = True
            try:
                cart = Cart.objects.get(customer = customer)
            except:
                cart = Cart.objects.create(
                            customer = customer,
                        )
                cart.session_id = cart.pk
                cart.save()
        else:  # customer = None
            if not cart_id:
                try:
                    cart = Cart.objects.create(
                        customer = customer,
                    )
                    cart.session_id = cart.pk
                    cart.save()
                except:
                    pass
            else:
                try:
                    cart = Cart.objects.get(session_id = self.request.session['cart'])
                except:
                    cart = Cart.objects.create(
                        customer = customer,
                        session_id = self.request.session['cart']
                    )
        # add a book to the cart
        book = Book.objects.get(pk = book_id)
        price = int(Book.objects.get(pk = book_id).price) * quantity

        book_in_cart, created = BookInCart.objects.get_or_create(
            cart = cart,
            book = book,
            defaults={
                'quantity': quantity,
                'price': price
            }
        )
        if not created:
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
        customer = self.request.user
        try:
            cart = Cart.objects.get(session_id = self.request.POST['session'])
            books = BookInCart.objects.filter(cart = cart)
        except:
            cart = Cart.objects.get(customer = customer)
            books = BookInCart.objects.filter(cart = cart)
        
        context['books'] = books
        
        total_price = 0
        for book in books:
            total_price += book.price
        context['total_price'] = total_price
        
        return context
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

        