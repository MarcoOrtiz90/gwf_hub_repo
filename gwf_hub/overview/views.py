from django.shortcuts import render

# Create your views here.

def overview(response):
    return render(response, "overview.html", {})

def database(response):
    return render(response, "database.html", {})

def validator(response):
    return render(response, "validator.html", {})

def hierarchy(response):
    return render(response, "hierarchy.html", {})