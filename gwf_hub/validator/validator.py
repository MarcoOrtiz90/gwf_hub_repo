import collections
from pathlib import Path
import json
import os
from collections import Counter
import operator as op


# c_section = json.loads(input("Insert the Sections JSON Code - "))
# c_questions = json.loads(input("Insert the Questions JSON Code - "))


def current_question_data(questions, sections, toggle_dict):
    print("Validator function is being called")
    c_questions = json.loads(questions)
    c_section = json.loads(sections)
    issues_string = ""
    c_question_group_bucket_duplicate = []
    duplicated_answer_ids = []
    c_question_group_bucket = []
    sections_id_bucket = []
    mandates = []
    q_group_ids = []
    wrong_answer_ids = []

    # This is a newer version of validator
    # Unpacking toggle values:
    # adding one more comment
    # Trying a new comment!
    auto_answers = toggle_dict["auto_answers"]
    duplicate_id = toggle_dict["duplicate_id"]
    jumps = toggle_dict["jumps"]
    inactive_q_group = toggle_dict["inactive_q_group"]
    wrong_jumps = toggle_dict["wrong_jumps"]
    mandates_not_connected = toggle_dict["mandates_not_connected"]

    print("auto_answers : " + auto_answers, "duplicate_id : " + duplicate_id, "jumps: " + jumps, "inactive_q_group: " +
          inactive_q_group, "mandates_not_connected: " + mandates_not_connected)
    duplicated_question_group_id = []
    for values, data in c_questions.items():
        if values not in q_group_ids:
            q_group_ids.append(values)
        else:
            duplicated_question_group_id.append(values)

    for values, data in c_section.items():
        sections_id_bucket.append(values)
        if "workflow_question_group_ids" in data:
            number_of_mandates = len(data["workflow_question_group_ids"])
            if number_of_mandates == 0:
                error_text = str(values + " does not contain any mandate question groups! ")
                mandates.append(error_text)
            for n in range(0, number_of_mandates):
                mandates.append(data['workflow_question_group_ids'][n])

    # ---------------*************----------------
    follow_up_bucket = []
    q_groups_with_no_parent = []
    c_question_id_bucket = []
    c_answer_id_bucket = []
    auto_answer = []
    jumps_used = []
    mandate_missing = []
    wrong_jumps_used = []
    for c_group_id, c_data in c_questions.items():
        c_question_group_bucket.append(c_group_id)
        # else:
        #     duplicated_question_group_id.append(c_group_id)
        c_length_of_questions = len(c_data["workflow_questions"])
        for x in range(0, c_length_of_questions):
            c_question_group_counter = c_group_id
            c_counter = 0
            if "radio_options" in c_data["workflow_questions"][x]["responses"][0]:
                c_length_of_answers = len(c_data["workflow_questions"][x]["responses"][0]["radio_options"])
            elif "checkbox_options" in c_data["workflow_questions"][x]["responses"][0]:
                c_length_of_answers = len(c_data["workflow_questions"][x]["responses"][0]["checkbox_options"])
            else:
                c_length_of_answers = 1
            c_question_ids = c_data["workflow_questions"][x]["id"]
            c_question_id_bucket.append(c_question_ids)
            for i in range(0, c_length_of_answers):
                if "radio_options" in c_data["workflow_questions"][x]["responses"][0]:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]["id"]
                    if "followup_question_group_ids" in \
                            c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter]:
                        length_of_followups = len(
                            c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter][
                                "followup_question_group_ids"])
                        for t in range(0, length_of_followups):
                            follow_ups = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter][
                                "followup_question_group_ids"][t]
                            follow_up_bucket.append(follow_ups)
                    if "next_node_override" in c_data["workflow_questions"][x]["responses"][0]["radio_options"][
                        c_counter]:
                        jump = c_data["workflow_questions"][x]["responses"][0]["radio_options"][c_counter][
                            "next_node_override"]
                        jumps_used.append(c_answer_ids)
                        if jump not in sections_id_bucket:
                            wrong_jumps_used.append(c_answer_ids)
                elif "checkbox_options" in c_data["workflow_questions"][x]["responses"][0]:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["checkbox_options"][c_counter]["id"]
                else:
                    c_answer_ids = c_data["workflow_questions"][x]["responses"][0]["id"]
                if c_answer_ids not in c_answer_id_bucket:
                    c_answer_id_bucket.append(c_answer_ids)
                else:
                    duplicated_answer_ids.append(c_answer_ids)
                if c_question_group_counter == c_group_id:
                    c_counter += 1
                else:
                    c_counter = 0
                i += 1
            if "answer_eval_attributes" in c_data["workflow_questions"][x]:
                auto_answer.append(c_group_id)
            x += 1
        if c_group_id not in duplicated_question_group_id:
            duplicated_question_group_id.append(c_group_id)
    duplicate_list = follow_up_bucket
    follow_up_bucket = []

    for items in duplicate_list:
        if items not in follow_up_bucket and items != '':
            follow_up_bucket.append(items)

    for items in c_question_group_bucket_duplicate:
        if items not in follow_up_bucket:
            q_groups_with_no_parent.append(items)

    # Checking if mandates from sections.json are present in the questions.json file.
    for items in mandates:
        if items not in c_question_group_bucket:
            if items is not None:
                mandate_missing.append(items)

    # for answers in c_answer_id_bucket:
    #     if answers.startswith("Q-"):
    #         wrong_answer_ids.append(answers)
    # if len(wrong_answer_ids) > 0:
    #     issues_string = issues_string + "Answer ID that starts with Q- " + str(wrong_answer_ids) + "\n"

    # Saving the answer outputs on str(issues_string) to return

    if wrong_jumps == "on":
        if len(wrong_jumps_used) > 0:
            issues_string = issues_string + "Answers using wrong jumps - " + str(wrong_jumps_used) + "\n"

    if auto_answers == "on":
        if len(auto_answer) > 0:
            issues_string = issues_string + "Questions using auto-answers : " + str(auto_answer) + "\n"

    if duplicate_id == "on":
        if len(duplicated_answer_ids) > 0:
            issues_string = issues_string + "Duplicate answer ids - " + str(duplicated_answer_ids) + "\n"

    if jumps == "on":
        if len(jumps_used) > 0:
            issues_string = issues_string + "Answers using Jumps - " + str(jumps_used) + "\n"

    if inactive_q_group == "on":
        if len(q_groups_with_no_parent) > 0:
            issues_string = issues_string + "Inactive question groups - " + str(q_groups_with_no_parent) + "\n"

    if mandates_not_connected == "on":
        if len(mandate_missing) > 0:
            issues_string = issues_string + "Missing mandates - " + str(mandate_missing) + "\n"

    print("Function being called to last!")
    return issues_string
