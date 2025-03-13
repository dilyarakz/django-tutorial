from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Takes a request -> provides a response
# It is basically a request handler
# Action 

def say_hello(request):
    return HttpResponse('Hello World!')