from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.SalesBooks
        fields = '__all__'
    
class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.SalesAuthors
        fields = '__all__'