from django.shortcuts import render
from django.http import HttpResponse
from . import validator

# Create your views here.


def overview(response):
    return render(response, "overview.html", {})


def database(response):
    return HttpResponse("<h1>this is GWF Database</h1>")


def validator_fun(response):
    
    if response.method == 'POST':
        sections_json = response.POST.get('jsonCodeSections')
        questions_json = response.POST.get('jsonCodeQuestions')

        # Collecting the validator variables from index.html
        auto_answers_toggle = request.POST.get('auto_answers', 'off')
        duplicate_id_toggle = request.POST.get('duplicate_id', 'off')
        jumps_toggle = request.POST.get('jumps_check', 'off')
        wrong_jumps_toggle = request.POST.get('wrong_jumps', 'off')
        inactive_q_group_toggle = request.POST.get('inactive_q_group', 'off')
        mandates_not_connected_toggle = request.POST.get('mandates_not_connected', 'off')

        # Dictionary to contain all the toggle switch values which is passed to validator.py
        toggle_dictionary = {"auto_answers": auto_answers_toggle,
                             "duplicate_id": duplicate_id_toggle,
                             "jumps": jumps_toggle,
                             "inactive_q_group": inactive_q_group_toggle,
                             "wrong_jumps": wrong_jumps_toggle,
                             "mandates_not_connected": mandates_not_connected_toggle}

        issues = validator.current_question_data(questions_json, sections_json, toggle_dictionary)
        issues_list = issues.split('\n')
        # print(issues_list)
        len_of_elements = len(issues_list) - 1
        issues_list.pop(len_of_elements)
        params = {"issues_to_print": issues_list}
        return render(request, 'validator_result.html', params)
    return render(response, "database.html", {})


def hierarchy(response):
    return render(response, "hierarchy.html", {})
