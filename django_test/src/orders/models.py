from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from books import models as book_models
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        related_name= "carts",
        verbose_name= "Customers",
        null = True,
        blank=True,
    )
    created_date = models.DateTimeField(
        verbose_name= "Created",
        auto_now= False,
        auto_now_add= True,
    )
    updated_date = models.DateTimeField(
        verbose_name= "Updated",
        auto_now= True,
        auto_now_add= False,
    )
    session_id = models.SmallIntegerField(
        verbose_name= "Session ID",
        null = True,
        blank=True,
    )

    def __str__(self) -> str:
        if self.customer:
            return str(self.customer) + ' in cart'
        else:
            return "Anonymous #" + str(self.session_id) + ' in cart'

class BookInCart(models.Model):
    cart = models.ForeignKey(
        'orders.Cart',
        on_delete = models.PROTECT,
        related_name= "goods",
        verbose_name= "Cart",
    )
    book = models.ForeignKey(
         book_models.Book,
        on_delete = models.PROTECT,
        related_name= "goods",
        verbose_name= "Book",
    )
    quantity = models.SmallIntegerField(
        verbose_name= "Quantity",
    )
    price = models.DecimalField(
        verbose_name= "Price",
        decimal_places=2,
        max_digits=7,
        null = True,
        blank=True,
    )
    created_date = models.DateTimeField(
        verbose_name= "Created",
        auto_now= False,
        auto_now_add= True,
    )
    updated_date = models.DateTimeField(
        verbose_name= "Updated",
        auto_now= True,
        auto_now_add= False,
    )
    def __str__(self) -> str:
        if self.cart.customer:
            return str(self.book.name) + ' in cart ' + str(self.cart.customer)
        else:
            return str(self.book.name) + ' in cart Anonymous #' + str(self.cart.session_id)
