from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1> ')

# Create your views here.

def about(request):
    return HttpResponse('<h1> About service</h1>')

def contact(request):
    return HttpResponse('<h1> contact service</h1>')

def other(request):
    return HttpResponse('<h1> other service</h1>')
