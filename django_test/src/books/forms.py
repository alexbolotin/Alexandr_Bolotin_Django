from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'