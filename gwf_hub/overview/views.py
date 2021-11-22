from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def overview(response):
    return render(response, "overview.html", {})

def database(response):
    return HttpResponse("<h1>this is GWF Database</h1>")
