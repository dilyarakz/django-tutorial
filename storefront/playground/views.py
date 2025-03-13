from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Takes a request -> provides a response
# It is basically a request handler
# Action 

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Dida'})