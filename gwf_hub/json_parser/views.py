from django.shortcuts import render
# Create your views here.


def json_parser(request):
    return render(request, 'json_parser.html')

