from django.shortcuts import HttpResponse, render
from random import randint
# Create your views here.
NAMES = ('Ivan', 'Kolia', 'Vasia')
def hello_world_view(words):
    name = NAMES[randint(0,2)]
    return HttpResponse(f"<h1>Hello {words.user}</h1>")