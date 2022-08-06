from requests import request
from books import models
from . import forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

#  Books
class BooksList(generic.ListView):
    template_name = "books/books_view.html"
    model = models.Book

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
    

class BookView(generic.DetailView):
    template_name = "books/book_view.html"
    model = models.Book
 
    def get_context_data(self,*args, **kwargs):

        def list_to_str(value):
            text = ''
            if len(value) == 1:
                text = value[0].name
            else:
                for author in value:
                    text += str(author.name) + '; '
            return text

        context = super().get_context_data(*args, **kwargs)

        book = models.Book.objects.get(pk = self.object.pk)
        context['author'] = list_to_str(book.author.all())
        context['genre'] = list_to_str(book.genre.all())
        
        return context

class BookAdd(PermissionRequiredMixin,generic.CreateView):
    template_name = "books/book_add.html"
    model = models.Book
    form_class = forms.AddBookForm
    permission_required = 'books.add_book'

    
    def get_success_url(self):
        return reverse_lazy("books:book-view", kwargs = {'pk' : self.object.pk})

class BookEdit(PermissionRequiredMixin,generic.UpdateView):
    template_name = "books/book_edit.html"
    model = models.Book
    form_class = forms.AddBookForm
    permission_required = 'books.change_book'

    def get_success_url(self):
        return reverse_lazy("books:book-view", kwargs = {'pk' : self.object.pk})

class BookDelete(PermissionRequiredMixin,generic.DeleteView):
    template_name = "books/book_delete.html"
    model = models.Book
    success_url = "/books/books_view/"
    permission_required = 'books.delete_book'
