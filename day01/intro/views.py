from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('This is my home page')


def view_home_page(request):
    return render(request, 'index.html')
