from django import forms
from . import models

# class AddBookForm(forms.ModelForm):
#     class Meta:
#         model = models.Book
#         fields = '__all__'
    
class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class AddPublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing_house
        fields = '__all__'

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'

class AddSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = '__all__'

class AddGenresForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'