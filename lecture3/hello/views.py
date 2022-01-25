from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'hello/index.html')


def greet(request, username):
    return render(request, 'hello/greet.html', {'username': username})
