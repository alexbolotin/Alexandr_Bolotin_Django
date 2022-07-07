from django.shortcuts import HttpResponse, render
from random import randint
import datetime
import time

# Create your views here.
NAMES = ('Ivan', 'Kolia', 'Vasia')


def hello_world_view(request):
    # name = NAMES[randint(0,2)]
    clock = datetime.datetime.now()
    time_str = clock.strftime("%H:%M:%S")
    return HttpResponse(f"<h1>Hello {request.user}</h1>\n<h1>Hello {time_str}</h1>")

