from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.shortcuts import resolve_url

from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your views here.

class LoginUserView(auth_views.LoginView):
    template_name = "auth_user/login.html"

    def get_default_redirect_url(self):
        url = reverse_lazy("books:book-view-all")              
        return resolve_url(url)

class LogoutUserView(auth_views.LogoutView):
    template_name = "directory/home_page.html"

    def get_next_page(self):
        previous = self.request.META.get('HTTP_REFERER')
        next_page = previous
        return next_page

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = request.POST.get("username")
            user = User.objects.get(username = user_name)
            print(user)
            my_group = Group.objects.get(name='Users') 
            user.groups.add(my_group)
            print(my_group)
            print(user.groups)
            return redirect('auth:login')

    
    context = {'form': form}

    return render(request, 'auth_user/registration.html', context)


    