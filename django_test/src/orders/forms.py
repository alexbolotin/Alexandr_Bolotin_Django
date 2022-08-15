from django import forms
from . import models

# class AddBookForm(forms.ModelForm):
#     class Meta:
#         model = models.Book
#         fields = '__all__'
    
class CartForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = '__all__'

class BookInCartForm(forms.ModelForm):
    class Meta:
        model = models.BookInCart
        fields = '__all__'