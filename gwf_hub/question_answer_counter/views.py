from django.shortcuts import render
from django.template import context
from numpy import number
##from . import automator


def questionCounter(request):
    context = {
        'main': 'yes',
        'bpmns': '',
        'payloadBpmn':''
    }

    if request.method == "POST":
        if request.POST.get('request_container'):
             requestAmount = request.POST['container_number']
             if requestAmount != '':
                 requestAmount = int(requestAmount)
                 context['bpmns'] = requestAmount
                 return render(request, 'questionCounter.html', context)
    
    return render(request, 'questionCounter.html', context)
