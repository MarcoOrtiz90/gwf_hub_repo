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
        if request.POST.get('bpmn_file'):
             pass
    
    return render(request, 'questionCounter.html', context)
