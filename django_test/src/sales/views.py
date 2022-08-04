from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import forms
from directory import models as dirs
from sales import models
from datetime import datetime
# Create your views here.

# Books

class SalesBooksView(generic.ListView):
    template_name = "sales/sales_books_view.html"
    model = models.SalesBooks
 
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['date'] = datetime.now().date
        return context

class SalesBookView(generic.DetailView):
    template_name = "sales/sales_book_view.html"
    model = models.SalesBooks
 
    def get_context_data(self,*args, **kwargs):
        sale = models.SalesBooks.objects.get(pk=self.object.pk)
        sale_books = sale.book.all()
        text = ''
        if len(sale_books) == 1:
                text = sale_books[0].name
        else:
            for author in sale_books:
                text += str(author.name) + '; '
    
        context = super().get_context_data(*args, **kwargs)
        context['books'] = text
        return context

class SalesBookAdd(generic.CreateView):
    template_name = "sales/sales_book_add.html"
    model = models.SalesBooks
    form_class = forms.AddBookForm
    
    def get_success_url(self):
        return reverse_lazy("sales:sales-books-view", kwargs = {'pk' : self.object.pk})

class SalesBookEdit(generic.UpdateView):
    template_name = "sales/sales_book_edit.html"
    model = models.SalesBooks
    form_class = forms.AddBookForm

    def get_success_url(self):
        return reverse_lazy("sales:sales-book-view", kwargs = {'pk' : self.object.pk})

class SalesBookDelete(generic.DeleteView):
    template_name = "sales/sales_book_delete.html"
    model = models.SalesBooks
    success_url = "/sales/sales_books_view/"


# Authors

class SalesAuthorsView(generic.ListView):
    template_name = "sales/sales_authors_view.html"
    model = models.SalesAuthors
 
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['date'] = datetime.now().date
        return context

class SalesAuthorView(generic.DetailView):
    template_name = "sales/sales_author_view.html"
    model = models.SalesAuthors
    
    def get_context_data(self,*args, **kwargs):
        sale = models.SalesAuthors.objects.get(pk=self.object.pk)
        sale_authors = sale.authors.all()
        text = ''
        if len(sale_authors) == 1:
                text = sale_authors[0].name
        else:
            for author in sale_authors:
                text += str(author.name) + '; '
    
        context = super().get_context_data(*args, **kwargs)
        context['authors'] = text
        return context

class SalesAuthorAdd(generic.CreateView):
    template_name = "sales/sales_author_add.html"
    model = models.SalesAuthors
    form_class = forms.AddAuthorForm
    
    def get_success_url(self):
        return reverse_lazy("sales:sales-author-view", kwargs = {'pk' : self.object.pk})

class SalesAuthorEdit(generic.UpdateView):
    template_name = "sales/sales_author_edit.html"
    model = models.SalesAuthors
    form_class = forms.AddAuthorForm

    def get_success_url(self):
        return reverse_lazy("sales:sales-author-view", kwargs = {'pk' : self.object.pk})

class SalesAuthorDelete(generic.DeleteView):
    template_name = "sales/sales_author_delete.html"
    model = models.SalesAuthors
    success_url = "/sales/sales_authors_view/"