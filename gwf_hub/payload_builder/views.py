from django.shortcuts import render

def payloadBuilder(request):
    return render(request, 'builder.html')
