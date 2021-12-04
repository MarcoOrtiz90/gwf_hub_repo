from .models import AutoAnswerQuestionTable, AutoAnswersTable

question_ids_table = AutoAnswerQuestionTable.objects.all()
answers_ids_table = AutoAnswersTable.objects.all()
import json

def genQuestionList(ids, expressions, order):
    main_q_list = ''
    if len(ids) > 1 :        
        for indx, id in enumerate(ids):
            listQuestion = ''
            openStrList = '['
            closeStrList = ']'
            openStrDict = '{'
            current = openStrDict + f'var: "{id}", '            
            for questions in question_ids_table:
                if id == questions.question_id:
                    current = current + f'category: {questions.question_category}, '
                    if questions.question_category == 'fup':
                        current = current + f'showExpression: "{expressions[indx]}", '
                    else:
                        current = current + f'showExpression: False, '
                    current = current + f'order: {order[indx]}' + '}'
                    questionResults = openStrList + current + closeStrList
                    listQuestion = listQuestion + questionResults
            main_q_list = main_q_list + listQuestion + ','
            main_q_list = main_q_list[:-1]
        finalOutput = 'var auto_answer_question_list = '+ '[' + main_q_list +']'
        print("===MAIN AFTER LOOP===")
        print(finalOutput)
            # main_q_list.append(listQuestion)
    #print(main_q_list)
    #print(type(main_q_list))
    #print("==JSON CODES==")
    #jsonData = json.dumps(main_q_list) line will become active at a later stage
    #print(jsonData)
    #print(type(jsonData))
    return(finalOutput)


def labels(questions):
    main_labels = ''    
    if len(questions) > 1 :
        for id in questions:
            current_label = ''
            for qID in question_ids_table:
                if id == qID.question_id:
                    current_label = f"'{qID.question_label}'"
                    main_labels = main_labels + current_label + ', '
        main_labels = main_labels[:-2]
        result_labels = 'var auto_answer_question_label_list = ' + '[' + main_labels + ']'
        print("===MAIN LABELS===")
        print(result_labels)
                      
    return (result_labels)

def answersGroup(questionIds):
    main_options = []
    if len(questionIds) > 1 :        
        for indx, ids in enumerate(questionIds): # ID OF THE INPUT..EJEM = Q-sa-age
            listAnswersStart = ''            
            for answer in answers_ids_table: # LOOP THROUGH THE ANSWERS TABLE
                # currentAnsw = ''
                # group = ''
                parentString = str(answer.parent_question)
                if parentString == ids: # CHECK IF CURRENT ANSWER PARENT ITERATION IS EQUAL TO CURRENT ID ITERATION
                    print("===CURRENT ANSWER==")
                    currentAnsw = f"message: '{answer.answer_label}', value:'{answer.answer_id}'"
                    currentAnsw = '{'+ currentAnsw + '}'
                    listAnswersStart = listAnswersStart + currentAnsw + ', '
                    
                listAnswersStart = listAnswersStart + listAnswersStart
                main_options= '[' + listAnswersStart + ']'
        # print("===Answers List FINAL===")
        # main_options= '[' + listAnswersStart + ']'
        # print(main_options)


                    # dictAnswer['message'] = answer.answer_label
                    # dictAnswer['value'] = answer.answer_id                    
                    # print("===Dictionary within loop===")
                    # print(dictAnswer)
        return (main_options)


def templateCreator(questions, labels, answers, dynamic):
    codeLogicStart = 'var dynamicKeysMap = ionSystem.newEmptyStruct(); for (var i = 0; i < auto_answer_question_list.length; i++){for (var j = 0; j < auto_answer_question_list[i].length; j++) {var auto_answer_result = document.get(auto_answer_question_list[i][j]["varname"] + "_auto_answer_result").toString(); var filteredOptions = options_list[i].filter(function (option) {return auto_answer_result.indexOf(option["value"]) != -1;}); var is_auto_answered = true; if (filteredOptions.length == 0){ is_auto_answered = false; filteredOptions = options_list[i];} var inputProperties = ionSystem.newEmptyList(); inputProperties.add(ionSystem.newString("BUTTON_SELECT")); var inputOptions = ionSystem.newEmptyList(); for (var k = 0; k < filteredOptions.length; k++) { var option = ionSystem.newEmptyStruct();  option.put("message").newString(filteredOptions[k]["message"]); option.put("value").newString(filteredOptions[k]["value"]); inputOptions.add(option);}  var dynamicKeysInput = ionSystem.newEmptyStruct() dynamicKeysInput.put("label").newString(auto_answer_question_label_list[i]);  dynamicKeysInput.put("type").newString("select_one");            dynamicKeysInput.put("order").newInt(auto_answer_question_list[i][j]["order"]); dynamicKeysInput.put("properties", inputProperties); dynamicKeysInput.put("options", inputOptions); if(auto_answer_question_list[i][j]["category"] == "fup") { dynamicKeysInput.put("conditionalShowExpression").newString(auto_answer_question_list[i][j]["showExpression"]) } if(is_auto_answered){ dynamicKeysInput.put("supplemental_info").newString("This is an auto-answered question, please select the option.") }  dynamicKeysMap.put(auto_answer_question_list[i][j]["varname"], dynamicKeysInput); }} var retVal = ionSystem.newEmptyStruct(); '
    codeLogincEnd = f'retVal.put("{dynamic}" + "_dynamic_keys", dynamicKeysMap); retVal;'
    codeLogic = codeLogicStart + codeLogincEnd
    questions_str = str(questions)
    labels_str = str(labels)
    answers_str = str(answers)
    template = f"var auto_answer_question_label_list = {questions} var auto_answer_question_label_list = {labels} var options_list = {answers}  {codeLogic} "
    return (template)    


def dataAnalysis(postInputs):    
    key_name_expression = 'expression-input-'
    key_name_order = 'order-input-'
    ids_to_call = []
    showExpressions = []
    order = []
    dynamic_key_name = postInputs['dynamic-key-name']    
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
    #question_list_template = genQuestionList(ids_to_call, showExpressions, order)
    #labels_list = labels(ids_to_call)
    answers_list = answersGroup(ids_to_call)
    # template = templateCreator(question_list_template, labels_list, answers_list, dynamic_key_name)
    return(answers_list)
                
    #print(ids_to_call)