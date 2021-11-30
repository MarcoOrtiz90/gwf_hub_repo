from django.shortcuts import render
# Create your views here.


def json_parser(request):
    return render(request, 'json_parser.html')


def call_parser(request):
    if request.method == 'POST':
        na = request.POST.get('region_na', 'off')
        eu = request.POST.get('region_eu', 'off')
        fe = request.POST.get('region_fe', 'off')
        region = ''
        if na == "on":
            region = "NA"
        if eu == "on":
            region = "EU"
        if fe == "on":
            region = "FE"
        workflow_id = request.POST.get('workflows')
        print(region)
        from . import web_automation
        status = web_automation.wf_id_data(workflow_id, region)
        print(status)
        return render(request, 'parsed_files.html')

