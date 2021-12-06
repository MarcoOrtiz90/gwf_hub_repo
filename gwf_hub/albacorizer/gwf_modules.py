def radio_template(a_id, answer, annos, fup, enf):
    a_id = a_id.replace(" ", "")
    a_id = a_id.strip()
    if type(answer) is str:
        answer = answer.strip()
    if type(annos) is str:
        annos = annos.strip()
    if type(fup) != float:
        fup = fup.replace(" ", "")
        fup = fup.strip()
        fup_list = fup.split(',')
    radio = {
        "id": a_id,
        "label": answer,
        "auto_annotation": annos
    }
    if type(fup) is str:
        radio['followup_question_group_ids'] = fup_list
    if type(enf) is str:
        enf = enf.replace(" ", "")
        enf = enf.strip()
        radio["next_node_override"] = enf
    return radio


def checkbox_template(a_id, answer, annos, fup, enf):
    a_id = a_id.replace(" ", "")
    a_id = a_id.strip()
    if type(answer) is str:
        answer = answer.strip()
    check = {
        "id": a_id,
        "label": answer,
        "auto_annotation": annos
    }
    if type(annos) is str:
        annos = annos.strip()
    if type(fup) is str:
        fup = fup.replace(" ", "")
        fup = fup.strip()
        check['followup_question_group_ids'] = fup
    if type(enf) is str:
        enf = enf.replace(" ", "")
        enf = enf.strip()
        check["next_node_override"] = enf
    return check


def textbox_template(a_id, answer):
    a_id = a_id.replace(" ", "")
    a_id = a_id.strip()
    textbox = {
        "id": a_id,
        "max_length": answer
    }
    return textbox


def aa_template(ruleset, schema):
    answer_eval_attributes = {
        "rule_set_name": ruleset,
        "schema_name": schema
    }

    return answer_eval_attributes


def workflow_questions_radio(question_id, question, radio_structure, auto_ruleset, auto_schema):
    attributes = "answer_eval_attribute"
    print(type(auto_schema))
    if type(question_id) != float:
        question_id.strip()
    questions_build = {
                "id": question_id,
                "question_string": question,
                "responses": [radio_structure]
            }
    if type(auto_schema) != float:
        values = aa_template(auto_ruleset, auto_schema)
        questions_build[attributes] = values
        print(questions_build)

    return questions_build


def workflow_questions_text(question_id, question, a_filled, auto_ruleset, auto_schema):
    attributes = "answer_eval_attribute"
    questions_build = {
                "id": question_id,
                "question_string": question,
                "responses": a_filled
            }
    if type(auto_schema) != float:
        values = aa_template(auto_ruleset, auto_schema)
        questions_build[attributes] = values
        print(questions_build)

    return questions_build


def answer_type_textbox(answer_id, answer, a_filled):
    answer_id = answer_id.replace(" ", "")
    answer_id = answer_id.strip()
    new_text = textbox_template(answer_id, answer)
    a_filled.append(new_text)


def answer_type(a_type, a_filled, answer_id, answer, annotations, fup_tag, enforcement_action):
    if a_type == 'radio':
        new_radio = radio_template(answer_id, answer, annotations, fup_tag, enforcement_action)
        a_filled.append(new_radio)

    else:
        new_check = checkbox_template(answer_id, answer, annotations, fup_tag, enforcement_action)
        a_filled.append(new_check)


def workflow_questions_checkbox(question_id, question, checkbox_structure, auto_ruleset, auto_schema):
    attributes = "answer_eval_attribute"
    questions_build = {
                "id": question_id,
                "question_string": question,
                "responses": [checkbox_structure]
            }
    if type(auto_schema) != float:
        values = aa_template(auto_ruleset, auto_schema)
        questions_build[attributes] = values
        print(questions_build)

    return questions_build


def sections_template(widgets_obj, section_name, next_section, widget_combination, question_groups):
    if type(question_groups) != float:
        question_groups = question_groups.replace(" ", "")
        question_groups = question_groups.strip()
    section = ''
    node_widgets = []
    print(widget_combination)
    w_c_split = widget_combination.split(',')
    for widget in w_c_split:
        widget = widget.lower()
        for index, row in widgets_obj.iterrows():
            widget_name = row['Widget Name'].lower()
            old_widget_id = row['Old Widget ID']
            shadow_widget = row['Shadow Widget']
            new_triton_widget = row['New Triton Widget ID']
            # weblab_a = row['weblab_a']
            if widget == widget_name:
                node_widgets.append(old_widget_id)
                node_widgets.append(shadow_widget)
                # if type(weblab_a) is str:
                #     node_widgets.append(weblab_a)
                if type(new_triton_widget) is str:
                    node_widgets.append(new_triton_widget)
    if type(question_groups) is str:
        question_groups_split = question_groups.split(',')
        section_wf = {
            "section_name": section_name,
            "workflow_question_group_ids": question_groups_split,
            "widgets_visible": node_widgets,
            "next_workflow_node": next_section
        }
        section = section_wf
    elif type(question_groups) is float:
        section_summary = {
            "widgets_visible": node_widgets
        }
        section = section_summary
    return section





