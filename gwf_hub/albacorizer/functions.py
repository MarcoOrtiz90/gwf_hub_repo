import pandas as pd
import openpyxl as xl
from . import gwf_modules as gwf
from PyQt5.QtWidgets import QMessageBox
import os


def question_answer_build(ms):
    q_and_a_section = {}  # dictionary that returns when questions function is called
    while True:
        try:
            df_ms = pd.read_excel(ms, sheet_name='master sheet')

        except:
            msg_mst = QMessageBox()
            msg_mst.setWindowTitle("Workbook Error")
            msg_mst.setText("Workbook does not have sheet named 'master sheet'")
            msg_mst.setIcon(QMessageBox.Warning)
            x = msg_mst.exec_()
            break

        current_q_g_id = 'none'
        current_q_id = 'none'
        current_question = 'none'
        current_answer_type = 'none'
        question_details = []
        question_structure = {
           "workflow_questions": question_details
        }
        radio_structure = {}
        checkbox_structure = {}
        a_filled = []
        group_eval = False
        prev_ans_type = ''
        current_q_dict_vals = []
        try:
            for index, row in df_ms.iterrows():
                question_group = row['Q group ID']
                enforcement_action = row['Jump']
                fup_tag = row['FUP Tag']
                question_id = row['Q ID']
                question = row['Question']
                answer_id = row['Answer ID']
                answer = row['Answer']
                answer_type = row['Answer Type']
                if answer_type == "textbox":
                    answer = int(answer)
                annotations = row['Annotations']
                summary = row['Section ID']
                auto_ruleset = row['Eval Ruleset']
                auto_schema = row['Eval Schema']
                # print("Answer - ", answer, " Answer-ID - ", annotations)
                if type(annotations) == float:
                    if answer_type != "textbox":
                        annotations = answer
                if type(question_group) is str:
                    if current_q_g_id != question_group or current_q_id != question_id:
                        if current_q_id != 'none':
                            if current_answer_type == 'radio':
                                radio_structure = {"radio_options": a_filled}
                                new_question_id = gwf.workflow_questions_radio(current_q_id, current_question, radio_structure, current_ruleset, current_schema)
                            elif current_answer_type == 'checkbox':
                                checkbox_structure = {
                                    "checkbox_options": a_filled,
                                    "min_selected": 0,
                                    "max_selected": 999
                                }
                                new_question_id = gwf.workflow_questions_checkbox(current_q_id, current_question, checkbox_structure, current_ruleset, current_schema)
                            elif current_answer_type == 'textbox':
                                new_question_id = gwf.workflow_questions_text(current_q_id, current_question, a_filled, current_ruleset, current_schema)
                            question_details.append(new_question_id)
                            if current_q_g_id != question_group:
                                question_structure = {
                                    "workflow_questions": question_details
                                }
                                question_details = []
                            q_and_a_section[current_q_g_id] = question_structure

                        if type(current_q_id) is not float:
                            current_q_id = question_id.strip()
                        else:
                            print(index)
                        if type(current_q_g_id) is not float:
                            current_q_g_id = question_group.strip()
                        else:
                            print(index)
                        # current_q_g_id = question_group
                        current_question = question
                        current_answer_type = answer_type
                        current_ruleset = auto_ruleset
                        current_schema = auto_schema
                        a_filled = []
                        print(answer)
                    if answer_type == 'radio':
                        gwf.answer_type(answer_type, a_filled, answer_id, answer, annotations, fup_tag, enforcement_action)
                    elif answer_type == 'textbox':
                        gwf.answer_type_textbox(answer_id, answer, a_filled)
                    else:
                        q_and_a_section[current_q_g_id] = gwf.answer_type(answer_type, a_filled, answer_id, answer, annotations, fup_tag, enforcement_action)
                elif summary == "node-summary":
                    if current_answer_type == 'radio':
                        radio_structure = {"radio_options": a_filled}
                        new_question_id = gwf.workflow_questions_radio(current_q_id, current_question, radio_structure, current_ruleset, current_schema)
                    elif current_answer_type == 'checkbox':
                        checkbox_structure = {
                            "min_selected": 0,
                            "max_selected": 999,
                            "checkbox_options": a_filled
                        }
                        new_question_id = gwf.workflow_questions_checkbox(current_q_id, current_question, checkbox_structure, current_ruleset, current_schema)
                    elif current_answer_type == 'textbox':
                        new_question_id = gwf.workflow_questions_text(current_q_id, current_question, a_filled, current_ruleset, current_schema)
                    question_details.append(new_question_id)
                    if current_q_g_id != question_group:
                        question_structure = {
                            "workflow_questions": question_details
                        }
                        question_details = []
                    q_and_a_section[current_q_g_id] = question_structure
        except KeyError:
            pass
        break

    return q_and_a_section


def section_build(ms):
    node_section = {}  # returned dictionary when sections is called
    while True:
        try:
            df_ms = pd.read_excel(ms, sheet_name='master sheet')
            df_wid = pd.read_excel(ms, sheet_name='widget ids')
        except:
            print("section error")
            break
        try:
            for index_ms, row_ms in df_ms.iterrows():
                widget_combination = row_ms["Widget Combination"]
                section_id = row_ms["Section ID"]
                section_name = row_ms["Section Name"]
                next_section = row_ms["NextSect"]
                question_groups = row_ms["Question groups"]
                if type(section_id) is str:
                    section = gwf.sections_template(df_wid, section_name, next_section, widget_combination, question_groups)
                    node_section[section_id] = section
        except KeyError:
            pass
        break
    return node_section


