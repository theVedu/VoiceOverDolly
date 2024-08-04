from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("<h1>Hey i am vibhu</h1>")



def success_page(request):
    return HttpResponse("<h1>Thanks for registration</h1>")