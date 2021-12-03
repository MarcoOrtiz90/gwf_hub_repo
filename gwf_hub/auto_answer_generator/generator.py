from typing import List, MutableMapping
from .models import AutoAnswerQuestionTable, AutoAnswersTable

question_ids_table = AutoAnswerQuestionTable.objects.all()
answers_ids_table = AutoAnswersTable.objects.all()
import json

def genQuestionList(ids, expressions, order):
    main_q_list = []
    if len(ids) > 1 :        
        for indx, id in enumerate(ids):
            listQuestion = []
            dictQuestion = {}
            dictQuestion['var'] = id
            for questions in question_ids_table:
                if id == questions.question_id:
                    dictQuestion['category'] = questions.question_category
                    if questions.question_category == 'fup':
                        dictQuestion['showExpression'] = expressions[indx]
                    else:
                        dictQuestion['showExpression'] = False
                    dictQuestion['order'] = order[indx]
            finalDict = dictQuestion.copy()
            listQuestion.append(finalDict)
            main_q_list.append(listQuestion)
    #print(main_q_list)
    #print(type(main_q_list))
    #print("==JSON CODES==")
    #jsonData = json.dumps(main_q_list) line will become active at a later stage
    #print(jsonData)
    #print(type(jsonData))
    return(main_q_list)


def labels(questions):
    main_labels = []
    if len(questions) > 1 :
        for list in questions:
            for dict in list:
                idOfDict = dict["var"]
                for question in question_ids_table:
                    # print("Question type")
                    # print(type(question))
                    # print(question)
                    if idOfDict == question.question_id:
                        main_labels.append(question.question_label)
    # print("===QUESTION LABELS===")                        
    # print(main_labels)                        
    return (main_labels)

def answersGroup(questionIds):
    main_options = []
    if len(questionIds) > 1 :        
        for indx, ids in enumerate(questionIds): # ID OF THE INPUT..EJEM = Q-sa-age
            listAnswers = []            
            for answer in answers_ids_table: # LOOP THROUGH THE ANSWERS TABLE
                dictAnswer = {}
                parentString = str(answer.parent_question)
                if parentString == ids: # CHECK IF CURRENT ANSWER PARENT ITERATION IS EQUAL TO CURRENT ID ITERATION
                    print("===")
                    print("===CURRENT DICT==")
                    print(dictAnswer)
                    print(answer.answer_label)
                    print(answer.answer_id)
                    dictAnswer['message'] = answer.answer_label
                    dictAnswer['value'] = answer.answer_id                    
                    # print("===Dictionary within loop===")
                    # print(dictAnswer)
                    listAnswers.append(dictAnswer)
                    print("===Current list===")
                    print(listAnswers)
            main_options.append(listAnswers)
        print("===FINAL OUTCOME===")
        print(main_options)
        return (main_options)


def dataAnalysis(postInputs):    
    key_name_expression = 'expression-input-'
    key_name_order = 'order-input-'
    ids_to_call = []
    showExpressions = []
    order = []
    dynamic_key_name = postInputs['dynamic-key-name']
    codeLogic = 'var dynamicKeysMap = ionSystem.newEmptyStruct(); for (var i = 0; i < auto_answer_question_list.length; i++){for (var j = 0; j < auto_answer_question_list[i].length; j++) {var auto_answer_result = document.get(auto_answer_question_list[i][j]["varname"] + "_auto_answer_result").toString(); var filteredOptions = options_list[i].filter(function (option) {return auto_answer_result.indexOf(option["value"]) != -1;}); var is_auto_answered = true; if (filteredOptions.length == 0){ is_auto_answered = false; filteredOptions = options_list[i];} var inputProperties = ionSystem.newEmptyList(); inputProperties.add(ionSystem.newString("BUTTON_SELECT")); var inputOptions = ionSystem.newEmptyList(); for (var k = 0; k < filteredOptions.length; k++) { var option = ionSystem.newEmptyStruct();  option.put("message").newString(filteredOptions[k]["message"]); option.put("value").newString(filteredOptions[k]["value"]); inputOptions.add(option);}  var dynamicKeysInput = ionSystem.newEmptyStruct() dynamicKeysInput.put("label").newString(auto_answer_question_label_list[i]);  dynamicKeysInput.put("type").newString("select_one");            dynamicKeysInput.put("order").newInt(auto_answer_question_list[i][j]["order"]); dynamicKeysInput.put("properties", inputProperties); dynamicKeysInput.put("options", inputOptions); if(auto_answer_question_list[i][j]["category"] == "fup") { dynamicKeysInput.put("conditionalShowExpression").newString(auto_answer_question_list[i][j]["showExpression"]) } if(is_auto_answered){ dynamicKeysInput.put("supplemental_info").newString("This is an auto-answered question, please select the option.") }  dynamicKeysMap.put(auto_answer_question_list[i][j]["varname"], dynamicKeysInput); }} var retVal = ionSystem.newEmptyStruct(); retVal.put("" + "_dynamic_keys", dynamicKeysMap); retVal;'
    for key in postInputs:
        if key.startswith(key_name_expression) == True:
            option = key.split('input-', 1)[1]            
            showExpressions.append(postInputs[key])
            print(postInputs[key])
    for keyOrder in postInputs:
        if keyOrder.startswith(key_name_order) == True:
            option = keyOrder.split('input-', 1)[1]
            ids_to_call.append(option)
            order.append(postInputs[keyOrder])
            print(postInputs[keyOrder])
        #print(ids_to_call)
    question_list_template = genQuestionList(ids_to_call, showExpressions, order)
    labels_list = labels(question_list_template)
    answers_list = answersGroup(ids_to_call)
    print(dynamic_key_name)
                
    #print(ids_to_call)