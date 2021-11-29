from django.shortcuts import render
# Create your views here.


def json_parser(request):
    print("json_parser() being called")
    return render(request, 'json_parser.html')


def call_parser(request):
    if request.method == 'POST':
        print("coming for call_parser function")
        workflow_id = request.POST.get('workflows')
        region = request.POST.get('region')
        from . import web_automation
        web_automation.wf_id_data(workflow_id, region)
        return render(request, 'parsed_files.html')

