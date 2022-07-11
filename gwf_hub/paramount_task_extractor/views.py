from django.http import request
from django.shortcuts import render
from django.template import context
from . import extractor
# Create your views here.


def taskExtractor(request):
    if request.method == "POST":
        origin_code = request.POST.get('origin_code')
        destination_code = request.POST.get('destination_code')
        tasks = request.POST.get('tasks_to_copy')
        output_code = str(extractor.extractorFunc(origin_code, destination_code, tasks))
        params = {"output_code": output_code}
        if output_code == '"':
            params = {"data_error": "Invalid Data, please try again with correct data!"}
        print(output_code)
        return render(request, 'task_extractor.html', params)
    return render(request, 'task_extractor.html')
