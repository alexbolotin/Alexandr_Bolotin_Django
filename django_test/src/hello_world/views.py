from django.shortcuts import HttpResponse, render
import datetime


# Create your views here.
NAMES = ('Ivan', 'Kolia', 'Vasia')


def hello_view(request):
    clock = datetime.datetime.now()
    time_str = clock.strftime("%H:%M:%S")
    return HttpResponse(f"<h1>Hello {request.user}</h1>\n<h1>Time of request - {time_str}</h1>")

