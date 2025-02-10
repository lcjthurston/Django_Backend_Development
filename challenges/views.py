from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. (they process response - they're a function that takes a request and sends back a response)

def index(request):
    return HttpResponse("This works!")