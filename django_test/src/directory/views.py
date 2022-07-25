from directory import models
from . import forms
from django.views import generic
from datetime import datetime
from django.urls import reverse_lazy

# Create your views here.
    
class Homepage(generic.TemplateView):
    template_name = "directory/home_page.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['date'] = datetime.now().date
        return context  

#  Books
class BooksList(generic.ListView):
    template_name = "directory/books_view.html"
    model = models.Book
 
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['date'] = datetime.now().date
        return context

class BookView(generic.DeleteView):
    template_name = "directory/book_view.html"
    model = models.Book
 
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['date'] = datetime.now().date
        return context

class BookAdd(generic.CreateView):
    template_name = "directory/book_add.html"
    model = models.Book
    form_class = forms.AddBookForm
    
    def get_success_url(self):
        return reverse_lazy("book-view", kwargs = {'pk' : self.object.pk})

class BookEdit(generic.UpdateView):
    template_name = "directory/book_edit.html"
    model = models.Book
    form_class = forms.AddBookForm

    def get_success_url(self):
        return reverse_lazy("book-view", kwargs = {'pk' : self.object.pk})

class BookDelete(generic.DeleteView):
    template_name = "directory/book_delete.html"
    model = models.Book
    success_url = "/books_view/"

# Authors
class AuthorView(generic.DeleteView):
    template_name = "directory/author_view.html"
    model = models.Author

class AuthorsList(generic.ListView):
    template_name = "directory/authors_view.html"
    model = models.Author

class AuthorEdit(generic.UpdateView):
    template_name = "directory/author_edit.html"
    model = models.Author
    form_class = forms.AddAuthorForm

    def get_success_url(self):
        return reverse_lazy("author-view", kwargs = {'pk' : self.object.pk})

class AuthorDelete(generic.DeleteView):
    template_name = "directory/author_delete.html"
    model = models.Author
    success_url = "/authors_view/"

class AuthorAdd(generic.CreateView):
    template_name = "directory/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    
    def get_success_url(self):
        return reverse_lazy("author-view", kwargs = {'pk' : self.object.pk})

# Publishings
class PublishingsList(generic.ListView):
    template_name = "directory/publishings_view.html"
    model = models.Publishing_house

class PublishingView(generic.DetailView):
    template_name = "directory/publishing_view.html"
    model = models.Publishing_house

class PublishingAdd(generic.CreateView):
    template_name = "directory/publishing_add.html"
    model = models.Publishing_house
    form_class = forms.AddPublishingForm

    def get_success_url(self):
        return reverse_lazy("publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingEdit(generic.UpdateView):
    template_name = "directory/publishing_add.html"
    model = models.Publishing_house
    form_class = forms.AddPublishingForm

    def get_success_url(self):
        return reverse_lazy("publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingDelete(generic.DeleteView):
    template_name = "directory/publishing_delete.html"
    model = models.Publishing_house
    success_url = "/publishings_view/"

# Series
class SeriesList(generic.ListView):
    template_name = "directory/serieses_view.html"
    model = models.Series

class SeriesView(generic.DetailView):
    template_name = "directory/series_view.html"
    model = models.Series

class SeriesAdd(generic.CreateView):
    template_name = "directory/series_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("series-view", kwargs = {'pk' : self.object.pk})

class SeriesEdit(generic.UpdateView):
    template_name = "directory/series_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("series-view", kwargs = {'pk' : self.object.pk})

class SeriesDelete(generic.DeleteView):
    template_name = "directory/series_delete.html"
    model = models.Series
    success_url = "/serieses_view/"

# 
# 