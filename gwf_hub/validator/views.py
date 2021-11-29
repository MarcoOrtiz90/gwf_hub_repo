from django.shortcuts import render, redirect
from . import validator

# Create your views here.
def validator_fun(request):
    if request.method == 'POST':
        sections_json = request.POST.get('sections_json')
        questions_json = request.POST.get('questions_json')

        if sections_json != '' or questions_json != '':
            try:
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
                                    "mandates_not_connected": mandates_not_connected_toggle
                }

                issues = validator.current_question_data(questions_json, sections_json, toggle_dictionary)
                issues_list = issues.split('\n')
                # print(issues_list)
                len_of_elements = len(issues_list) - 1
                issues_list.pop(len_of_elements)
                params = {"issues_to_print": issues_list,
                          "return_questions_data": questions_json,
                          "return_sections_data": sections_json}
                print(params["return_sections_data"])
                return render(request, 'validator.html', params)
            except ValueError:
                issues_list = "Invalid/Incomplete JSON Codes entered. Please check the \ncodes and try again."
                params = {"issues_to_print": issues_list,
                          "return_questions_data": questions_json,
                          "return_sections_data": sections_json}
                print(params["return_sections_data"])
                return render(request, 'validator.html', params)
        else:
            issues_list = "Please insert JSON data in the textboxes and try again."
            params = {"issues_to_print": issues_list,
                      "return_questions_data": questions_json,
                      "return_sections_data": sections_json}
            return render(request, 'validator.html', params)

    return render(request, 'validator.html', {})