from django.shortcuts import render

# Create your views here.
def aaGenerator(request):
    return render(request, "generator.html", {})