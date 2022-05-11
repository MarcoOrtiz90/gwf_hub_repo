from distutils.log import error
import pandas as pd
import openpyxl as xl

def buildPayload():    
    payload = '' # final payload output to return
    dataFile = pd.read_excel('paramount_enforcement_api_data.xlsx', sheet_name='QuestionData')
    valStart = '${&#34;'
    valEnd = '&#34;}'
    camundaValString = '<camunda:in sourceExpression=\\"'
    camundaValVar = '<camunda:in source=\\"'
    print(dataFile)

    for idx, row in dataFile.iterrows():
        idx+=1
        step = row['Step']
        question = row['Question String']
        answer = row['Answer ID']
        if idx >= 10 :
            targetS = f'\\" target=\\"question_stringId_{idx}\\" />'
            targetP = f'\\" target=\\"question_stepId_{idx}\\" />'
            targetA = f'\\" target=\\"question_answer_{idx}\\" />'
        else:
            targetS = f'\\" target=\\"question_stringId_0{idx}\\" />'
            targetP = f'\\" target=\\"question_stepId_0{idx}\\" />'
            targetA = f'\\" target=\\"question_answer_0{idx}\\" />'

        valStep = camundaValString+valStart+step+valEnd+targetP
        valQuestion = camundaValString+valStart+question+valEnd+targetS
        valAnswer = camundaValVar+answer+targetA
        iterationString = valQuestion+valStep+valAnswer

        if not payload:                                     
            payload = iterationString
        else:
            payload = payload + iterationString

    print(payload)

buildPayload()
    