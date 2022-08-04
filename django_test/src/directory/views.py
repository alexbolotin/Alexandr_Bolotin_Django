from requests import request
from directory import models
from . import forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
    
class Homepage(generic.TemplateView):
    template_name = "directory/home_page.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context  
        

# Authors
class AuthorView(generic.DetailView):
    template_name = "directory/author_view.html"
    model = models.Author

class AuthorsList(generic.ListView):
    template_name = "directory/authors_view.html"
    model = models.Author

class AuthorEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "directory/author_edit.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = '/auth/login'
    # redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy("dirs:author-view", kwargs = {'pk' : self.object.pk})

class AuthorDelete(generic.DeleteView):
    template_name = "directory/author_delete.html"
    model = models.Author
    success_url = "/dirs/authors_view/"

class AuthorAdd(generic.CreateView):
    template_name = "directory/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    
    def get_success_url(self):
        return reverse_lazy("dirs:author-view", kwargs = {'pk' : self.object.pk})

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
        return reverse_lazy("dirs:publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingEdit(generic.UpdateView):
    template_name = "directory/publishing_edit.html"
    model = models.Publishing_house
    form_class = forms.AddPublishingForm

    def get_success_url(self):
        return reverse_lazy("dirs:publishing-view", kwargs = {'pk' : self.object.pk})

class PublishingDelete(generic.DeleteView):
    template_name = "directory/publishing_delete.html"
    model = models.Publishing_house
    success_url = "/dirs/publishings_view/"

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
        return reverse_lazy("dirs:series-view", kwargs = {'pk' : self.object.pk})

class SeriesEdit(generic.UpdateView):
    template_name = "directory/series_edit.html"
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("dirs:series-view", kwargs = {'pk' : self.object.pk})

class SeriesDelete(generic.DeleteView):
    template_name = "directory/series_delete.html"
    model = models.Series
    success_url = "/dirs/serieses_view/"

# 
# Genres
class GenresList(generic.ListView):
    template_name = "directory/genres_view.html"
    model = models.Genre

class GenreView(generic.DetailView):
    template_name = "directory/genre_view.html"
    model = models.Genre

class GenreAdd(generic.CreateView):
    template_name = "directory/genre_add.html"
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("dirs:genre-view", kwargs = {'pk' : self.object.pk})

class GenreEdit(generic.UpdateView):
    template_name = "directory/genre_edit.html"
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("dirs:genre-view", kwargs = {'pk' : self.object.pk})

class GenreDelete(generic.DeleteView):
    template_name = "directory/genre_delete.html"
    model = models.Genre
    success_url = "/dirs/genres_view/"