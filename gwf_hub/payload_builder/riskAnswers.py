import pandas as pd
import os

# workflowIDs = []

idsDirectory = 'C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/excelToCheck'

# for file in os.listdir(idsDirectory):
#     if file not in workflowIDs:
#         workflowIDs.append(file)

# print(workflowIDs)

question_labels = ['Provide Name/Address/Phone/Token which are verified with bank', 'Provide IV link', 'Additional Annotations', 'What information verified with Bank?', 'Provide Customer contact number and Manual annotation to mention with whom inv spoke either ACH/CCH and to provide extra info mentioned by customer', 'What is the token tail?', 'Provide Customer contact number and additional information provided by customer' ]

risky_workflows = []

labelsFrequency = []

def verifyWorkflows():
    for wfid in os.listdir(idsDirectory):
        dataFile = pd.read_excel(f'C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/excelToCheck/{wfid}', sheet_name='master sheet')
        for idx, row in dataFile.iterrows():
            idx+=1
            question = row['Question']
            answer_type = row['Answer Type']
            if answer_type == 'textbox':
                for label in question_labels:
                    if question == label:
                        if wfid not in risky_workflows:
                            risky_workflows.append(wfid)
                        labelsFrequency.append(question)

    df_wfs = pd.DataFrame(risky_workflows)
    df_lablfreq = pd.DataFrame(labelsFrequency)
    print('Risky Workflows')
    print(df_wfs)
    print('Question Frequency')
    print(df_lablfreq)

    df_wfs.to_excel('riskyWorkflows.xlsx')
    df_lablfreq.to_excel('frequency.xlsx')

verifyWorkflows()