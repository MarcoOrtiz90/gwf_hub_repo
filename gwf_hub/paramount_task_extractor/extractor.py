import os
import getpass
from pathlib import Path


def extractorFunc(source_bpmn_code, bpmn_code, user_task_list):
    user_task_list = user_task_list
    source_bpmn_code = source_bpmn_code
    bpmn_code = bpmn_code
    xml_string = ''
    line = ''
    code = ''
    output1 = Path('source_bpmn_code.txt')
    output2 = Path('destination_code.txt')
    if output1.is_file():
        os.remove('source_bpmn_code.txt')

    if output2.is_file():
        os.remove('destination_code.txt')

    os.system('nul > source_bpmn_code.txt')
    os.system('nul > destination_code.txt')

    with open(file='source_bpmn_code.txt', encoding='UTF-8', mode='w') as f:
        f.write(source_bpmn_code)
        f.close()

    with open(file='source_bpmn_code.txt', encoding='UTF-8', mode='r') as xml_file:
        for lines in xml_file:
            for words in lines:
                if words != '>':
                    line += words
                if words == '>':
                    line = line + '>'
                    xml_string += line + '\n'
                    line = ''


    with open(file='source_bpmn_code.txt', encoding='UTF-8', mode='w') as f:
        f.write(xml_string)
        f.close()

    user_task = user_task_list.split(',')
    task_condition = False
    task_code = ''
    shape_code = ''
    task_id = ''
    # print(xml_string)
    for tasks in user_task:
        task_property = ''
        task_condition = False
        task_shape = ''
        shape_condition = False
        with open(file='source_bpmn_code.txt', encoding='UTF-8', mode='r') as input_file:
            for lines in input_file:
                # Capturing the property for BPMN task on the flow
                if task_condition is True:
                    task_property = task_property + lines

                if tasks in lines and "<bpmn:userTask id=" in lines:
                    split_vars = lines.split('\\')
                    name_of_task = split_vars[3].replace('&#10;', '').strip('"')
                    # if '&' in name_of_task:
                    #     split_name = name_of_task.split('&')
                    #     name_of_task = split_name[0]
                    print(name_of_task)
                    if tasks == name_of_task:
                        task_property = task_property + lines

                        # Capturing the task ID for the task in the below 2 lines:
                        line_list_property = lines.split('"')
                        task_id = line_list_property[1].rstrip('\\')
                        print(task_id)
                        task_condition = True

                if '</bpmn:userTask>' in lines and task_condition is True:
                    task_code += task_property
                    task_condition = False

                # Capturing the data for BPMN task Shape on the flow
                if shape_condition is True:
                    task_shape += lines

                if '<bpmndi:BPMNShape id=' in lines and task_id in lines:
                    task_shape += lines
                    shape_condition = True

                if '</bpmndi:BPMNShape>' in lines and shape_condition is True:
                    shape_code += task_shape
                    break

                # Two variables holding the full script - shape_code, task_code which later gets copied to the final script

                # At this point the codes for the task have already been copied, now we paste the task code on the
                # destination BPMN codes.


    xml_string = ''
    line = ''

    for lines in bpmn_code:
        for words in lines:
            if words != '>':
                line += words
            if words == '>':
                line = line + '>'
                xml_string += line + '\n'
                line = ''

    with open(file="destination_code.txt", encoding='UTF-8', mode='w') as output_file:
        output_file.write(xml_string)
        output_file.close()

    bpmn_paste_code = False
    shape_paste_code = False
    updated_code = ''
    bpmn_task = 'not_completed'
    shape_task = 'not_completed'

    with open(file="destination_code.txt", encoding='UTF-8', mode='r') as output_file:
        for lines in output_file:
            updated_code += lines
            # For pasting the task code
            if '</bpmn:startEvent>' in lines and bpmn_task == 'not_completed':
                bpmn_paste_code = True
            if bpmn_paste_code is True:
                updated_code += task_code
                bpmn_paste_code = False
                bpmn_task = 'completed'

            # For pasting the shape code
            if '</bpmndi:BPMNShape>' in lines and shape_task == 'not_completed':
                shape_paste_code = True
            if shape_paste_code is True:
                updated_code += shape_code
                shape_paste_code = False
                shape_task = 'completed'

    with open(file='destination_code.txt', encoding='UTF-8', mode='w') as final:
        final.write(updated_code)
        final.close()

    with open(file='destination_code.txt', encoding='UTF-8', mode='r') as final:
        for lines in final:
            code += lines.rstrip('\n')
    code += '"'
    return code

