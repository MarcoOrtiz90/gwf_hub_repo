import pandas as pd
import os

idsDirectory = 'C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/excelToCheck'
workflowIdList = []
questionLabelList = []
questionIdList = []
rulesetList = []
frequency = {}

def autoAnswerAudit():
    for wfid in os.listdir(idsDirectory):
        ## print(wfid)
        dataFile = pd.read_excel(f'C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/excelToCheck/{wfid}', sheet_name='master sheet')
        for idx, row in dataFile.iterrows():
            idx+=1
            questionLabel = row['Question']
            questionId = row['Q ID']
            ruleset = row['Eval Ruleset']
            if pd.isna(ruleset) is False:  ## pd.isna() checks if the given variable is nan. Outputs True or False
                workflowIdList.append(wfid)
                questionLabelList.append(questionLabel)
                questionIdList.append(questionId)
                rulesetList.append(ruleset)
    
    dataForFrame = {
        'Workflow ID': workflowIdList,
        'Question Label': questionLabelList,
        'Question ID': questionIdList,
        'Eval Ruleset': rulesetList
    }

    for eval_ruleset in rulesetList:
        if eval_ruleset in frequency:
            frequency[eval_ruleset] += 1
        else:
            frequency[eval_ruleset] = 1

    print(frequency)

    dataFrame = pd.DataFrame(dataForFrame)

    frequencyFrame = pd.DataFrame(frequency, index=[0])

    print(dataFrame)
    print(frequencyFrame)

    dataFrame.to_excel('C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/aa_audit_b2b.xlsx', index=False)

    frequencyFrame.to_excel('C:/Users/mttrejos/Desktop/Amazon/gwf_hub_repo/gwf_hub/payload_builder/aa_frequency_b2b.xlsx', index=False)



autoAnswerAudit()