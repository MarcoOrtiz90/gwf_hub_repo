from django.shortcuts import render
from django.template import context
##from . import automator


def questionCounter(request):
    context = {
        'main': 'yes',
        'bpmns': '',
        'payloadBpmn':''
    }
    return render(request, 'questionCounter.html', context)

# Create your views here.
