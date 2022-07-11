from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from . import web_automation
from . import parser_main
from django.http import JsonResponse

# Create your views here.


def call_parser(request):
    status = ''
    try:
        if request.method == 'POST':
            counter = 0
            na = request.POST.get('region_na', 'off')
            eu = request.POST.get('region_eu', 'off')
            fe = request.POST.get('region_fe', 'off')
            chrome_browser = request.POST.get('chrome', 'off')
            firefox_browser = request.POST.get('firefox', 'off')

            # If more than one browser is used
            if (firefox_browser == "on") and (chrome_browser == "on"):
                e = "Please select only one browser"
                error_generated = "Exception generated - " + e
                error_msg = {"error": error_generated}
                return render(request, 'json_parser.html', error_msg)

            if chrome_browser == "on":
                browser_used = "Chrome"
            if firefox_browser == "on":
                browser_used = "Firefox"
            region = ''
            if na == "on":
                region = "NA"
                counter += 1
            if eu == "on":
                region = "EU"
                counter += 1
            if fe == "on":
                region = "FE"
                counter += 1

            # If more than one regions are selected
            if counter > 1:
                e = "Please select not more than one region at a time."
                error_generated = "Exception generated - " + e
                error_msg = {"error": error_generated}
                return render(request, 'json_parser.html', error_msg)

            workflow_id = request.POST.get('workflows')

            # If no workflow ID is present
            if workflow_id == "":
                e = "No Workflow Ids to generate!"
                error_generated = "Exception generated - " + e
                error_msg = {"error": error_generated}
                return render(request, 'json_parser.html', error_msg)

            web_automation.wf_id_data(workflow_id, region, browser_used)
            completion_message = "Your source files have successfully been created for the flows - " + str(workflow_id)
            returning_msg = {'message_to_display': completion_message}
            return render(request, 'json_parser.html', returning_msg)
    except Exception as e:
        e = str(e)
        error_generated = "Exception generated - " + e
        error_msg = {"error": error_generated}
        return render(request, 'json_parser.html', error_msg)    

    return render(request, 'json_parser.html')
