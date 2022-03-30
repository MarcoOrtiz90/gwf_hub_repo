from django.shortcuts import render
from django.template import context

# Create your views here.
def taskExtractor(response):
    if response.method == "POST":
        second_context = {
            "results": True
        }
        return render(response, 'task_extractor.html', second_context)
    return render(response, 'task_extractor.html', {})