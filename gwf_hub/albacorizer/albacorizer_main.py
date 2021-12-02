from . import functions
questions_file_name = ''
sections_file_name = ''
workflow_id_name = ''
import json


def new_ms_albacorize(source_file):
    global questions_file_name, sections_file_name, workflow_id_name
    root_ms_file = source_file
    questions = json.dumps(functions.question_answer_build(root_ms_file))
    if len(questions) == 0:
        print("No questions data")
    sections = json.dumps(functions.section_build(root_ms_file))
    if len(sections) == 0:
        print("No sections data")
    data_dict = {"questions_json": questions,
                 "sections_json": sections}
    return data_dict
