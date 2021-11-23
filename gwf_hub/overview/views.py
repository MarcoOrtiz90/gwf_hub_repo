from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def overview(response):
    return render(response, "overview.html", {})

def database(response):
    return HttpResponse("<h1>this is GWF Database</h1>")


def validator(response):
    
    if response.method == 'POST':
        sections_json = response.POST.get('jsonCodeSections')
        questions_json = response.POST.get('jsonCodeQuestions')

        # Collecting the validator variables from index.html
        auto_answers = request.POST.get('auto_answers', 'off')
        duplicate_id = request.POST.get('duplicate_id', 'off')
        jumps = request.POST.get('jumps_check', 'off')
        inactive_q_group = request.POST.get('inactive_q_group', 'off')
        mandates_not_connected = request.POST.get('mandates_not_connected', 'off')
        # print(auto_answers)

        issues = validator.current_question_data(questions_json, sections_json)
        issues_list = issues.split('\n')
        # print(issues_list)
        len_of_elements = len(issues_list) - 1
        issues_list.pop(len_of_elements)
        params = {"issues_to_print": issues_list}
        return render(request, 'validator_result.html', params)
    return render(response, "validator.html", {})