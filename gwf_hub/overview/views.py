from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def overview(response):
    name = "GWF App Dashboard"    
    return render(response, "overview.html", {'name':name})

def database(response):
    return HttpResponse("<h1>this is GWF Database</h1>")
