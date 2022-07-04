xml_string = ''
line = ''

with open(file='parammount.xml', mode='r', encoding='UTF-8') as xml_code:
    for lines in xml_code:
        for words in lines:
            if words != '>':
                line += words
            if words == '>':
                line = line + '>'
                xml_string += line + '\n'
                line = ''
    xml_code.close()

with open(file='parammount.xml', mode='w', encoding='UTF-8') as xml_code:
    xml_code.write(xml_string)
    xml_code.close()

status = ''
bpmn_string = ''
bpmn_dictionary_data = {}

with open(file='parammount.xml', mode='r', encoding='UTF-8') as xml_code:
    for lines in xml_code:
        # Capturing the section ID
        if '<bpmn:userTask id=' in lines and 'implementation' in lines:
            status = 'IN'
            section_id_list = lines.split('\\')
            section_id = str(section_id_list[3])
            section_id = section_id.replace('&#10;', '').lstrip('"')
        # Capturing the question and question ID
        if 'YES_NO_QUESTION' in lines:
            if status == 'IN':
                question_data = lines.split('"')
                question = question_data[3].strip('\\')

                question_id = question_data[1].strip('\\')

                bpmn_string = bpmn_string + question + " {{" + question_id + "}}, "

        if 'SELECT_BUTTON' in lines:
            if status == 'IN':
                question_data = lines.split('"')
                question = question_data[3].strip('\\')

                question_id = question_data[1].strip('\\')

                bpmn_string = bpmn_string + question + " {" + question_id + "}, "
        # Coming out of the condition if the code changes for section
        if "</bpmn:userTask>" in lines:
            status = "OUT"
            bpmn_string = bpmn_string.rstrip(", ")
            bpmn_dictionary_data.update({section_id: bpmn_string})
            bpmn_string = ''


for section, data in bpmn_dictionary_data.items():
    print(section + ": " + data + '\n')


