from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def call_parser(request):
    status = ''
    try:
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
            if workflow_id == '':
                print("No workflows added")
                messages.info(request, 'No Workflow Ids to generate!')
                return render(request, 'json_parser.html', )
            from . import web_automation
            web_automation.wf_id_data(workflow_id, region)
            completion_message = "Your source files have successfully been created for the flows - " + str(workflow_id)
            returning_msg = {'message_to_display': completion_message}
            return render(request, 'json_parser.html', returning_msg)
    except Exception as e:
        print("Key Error caught")
        e = str(e)
        error_generated = "Exception generated - " + e
        error_msg = {"error": error_generated}
        return render(request, 'json_parser.html', error_msg)
    return render(request, 'json_parser.html')
