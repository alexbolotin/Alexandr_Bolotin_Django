from directory import models
from . import forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from books import models as book_models

# Create your views here.
    
class Homepage(generic.TemplateView):
    template_name = "directory/home_page.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user)
        books = book_models.Book.objects.all()
        context['books'] = books      
        return context  
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)

# Authors
class AuthorView(generic.DetailView):
    template_name = "directory/author_view.html"
    model = models.Author

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = book_models.Book.objects.filter(author=self.object.pk)
        context['books'] = books      
        return context
    
class AuthorsList(generic.ListView):
    template_name = "directory/authors_view.html"
    model = models.Author

class AuthorEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "directory/author_edit.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = '/auth/login'
    permission_required = 'directory.change_author'

    def get_success_url(self):
        return reverse_lazy("dirs:author-view", kwargs = {'pk' : self.object.pk})

class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "directory/author_delete.html"
    model = models.Author
    success_url = "/dirs/authors_view/"
    permission_required = 'directory.delete_author'

class AuthorAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "directory/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    permission_required = 'directory.add_author'

    def get_success_url(self):
        return reverse_lazy("dirs:author-view", kwargs = {'pk' : self.object.pk})

# Publishings
class PublishingsList(generic.ListView):
    template_name = "directory/publishings_view.html"
    model = models.Publishing_house

class PublishingView(generic.DetailView):
    template_name = "directory/publishing_view.html"
    model = models.Publishing_house

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = book_models.Book.objects.filter(publishing=self.object.pk)
        context['books'] = books        
        return context

class PublishingAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "directory/publishing_add.html"
    model = models.Publishing_house
    form_class = forms.AddPublishingForm
    permission_required = 'directory.add_publishing_house'

    def get_success_url(self):
        return reverse_lazy("dirs:publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "directory/publishing_edit.html"
    model = models.Publishing_house
    form_class = forms.AddPublishingForm
    permission_required = 'directory.change_publishing_house'

    def get_success_url(self):
        return reverse_lazy("dirs:publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "directory/publishing_delete.html"
    model = models.Publishing_house
    success_url = "/dirs/publishings_view/"
    permission_required = 'directory.delete_publishing_house'

# Series
class SeriesList(generic.ListView):
    template_name = "directory/serieses_view.html"
    model = models.Series

class SeriesView(generic.DetailView):
    template_name = "directory/series_view.html"
    model = models.Series
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = book_models.Book.objects.filter(series=self.object.name)
        context['books'] = books      
        return context

class SeriesAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "directory/series_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm
    permission_required = 'directory.add_series'

    def get_success_url(self):
        return reverse_lazy("dirs:series-view", kwargs = {'pk' : self.object.pk})

class SeriesEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "directory/series_edit.html"
    model = models.Series
    form_class = forms.AddSeriesForm
    permission_required = 'directory.change_series'

    def get_success_url(self):
        return reverse_lazy("dirs:series-view", kwargs = {'pk' : self.object.pk})

class SeriesDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "directory/series_delete.html"
    model = models.Series
    success_url = "/dirs/serieses_view/"
    permission_required = 'directory.delete_series'

# 
# Genres
class GenresList(generic.ListView):
    template_name = "directory/genres_view.html"
    model = models.Genre

class GenreView(generic.DetailView):
    template_name = "directory/genre_view.html"
    model = models.Genre

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = book_models.Book.objects.filter(genre=self.object.pk)
        context['books'] = books      
        return context


class GenreAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "directory/genre_add.html"
    model = models.Genre
    form_class = forms.AddGenreForm
    permission_required = 'directory.add_genre'

    def get_success_url(self):
        return reverse_lazy("dirs:genre-view", kwargs = {'pk' : self.object.pk})

class GenreEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "directory/genre_edit.html"
    model = models.Genre
    form_class = forms.AddGenreForm
    permission_required = 'directory.change_genre'

    def get_success_url(self):
        return reverse_lazy("dirs:genre-view", kwargs = {'pk' : self.object.pk})

class GenreDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "directory/genre_delete.html"
    model = models.Genre
    success_url = "/dirs/genres_view/"
    permission_required = 'directory.delete_genre'
