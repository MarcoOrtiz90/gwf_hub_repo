from .models import AutoAnswerQuestionTable, AutoAnswersTable
question_ids_table = AutoAnswerQuestionTable.objects.all()
answers_ids_table = AutoAnswersTable.objects.all()

def genQuestionList(ids, expressions, order):
    main_q_list = ''
    if len(ids) > 1 :        
        for indx, id in enumerate(ids):
            print("===index debugging - first loop - ==")
            print(indx)
            print(expressions)
            listQuestion = ''
            openStrList = '['
            closeStrList = ']'
            openStrDict = '{'
            current = openStrDict + f'var: "{id}", '            
            for questions in question_ids_table:
                if id == questions.question_id:
                    print("===within for and if statement===")                    
                    current = current + f'category: "{questions.question_category}", '
                    if questions.question_category == 'fup':
                        print("---entered if statement for category---")
                        print(indx)
                        print(expressions)
                        current = current + f'showExpression: "{expressions[indx]}", '
                    else:
                        current = current + f'showExpression: False, '
                    current = current + f'order: {order[indx]}' + '}'
                    questionResults = openStrList + current + closeStrList + ', \n'
                    listQuestion = listQuestion + questionResults
            main_q_list = main_q_list + listQuestion + ','
            main_q_list = main_q_list[:-1]
        finalOutput = 'var auto_answer_question_list = ' + '[\n' + main_q_list +'] \n'        
    else: 
        current = '{' + f'var: "{ids}", '
        for questions in question_ids_table:
            if ids == questions.question_id:
                current = current + f'category: "{questions.question_category}", '
                if questions.question_category == 'fup':
                    current = current + f'showExpression: "{expressions}", '
                else:
                    current = current + f'showExpression: False, '
                current = current + f'order: {order}' + '}'
        current = '[\n' + current + '\n]'
        finalOutput = 'var auto_answer_question_list = ' + current
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
        main_labels = main_labels + '\n'
        result_labels = 'var auto_answer_question_label_list = ' + '[\n' + main_labels + ']\n'
    else:
        result_labels = ''
        for qID in question_ids_table:
            if questions == qID.question_id:
                current_label = f"'{qID.question_label}'"
                main_labels = current_label
                result_labels = 'var auto_answer_question_label_list = ' + '[\n' + main_labels + ']\n'
                      
    return (result_labels)

def answersGroup(questionIds):
    main_options = ''
    if len(questionIds) > 1 :        
        for indx, ids in enumerate(questionIds): # ID OF THE INPUT..EJEM = Q-sa-age
            listAnswersStart = ''            
            for answer in answers_ids_table: # LOOP THROUGH THE ANSWERS TABLE
                parentString = str(answer.parent_question)
                if parentString == ids: # CHECK IF CURRENT ANSWER PARENT ITERATION IS EQUAL TO CURRENT ID ITERATION
                    currentAnsw = f"message: '{answer.answer_label}', value:'{answer.answer_id}'"
                    currentAnsw = '{'+ currentAnsw + '}'
                    listAnswersStart = listAnswersStart + currentAnsw + ', '            
            listAnswersStart = listAnswersStart[:-2]
            listAnswersStart = '[' + listAnswersStart + '], '
            main_options = main_options + listAnswersStart
        main_options = main_options[:-2]
        main_options = main_options + '\n'
        main_options = 'var options_list = ' + '[\n' + main_options + ']\n '
    else:
        print("got in else")
        listAnswersStart = ''
        for item in questionIds:       
            for idx, answer in enumerate(answers_ids_table):
                parentString = str(answer.parent_question)
                if parentString == item:
                    currentAnsw = f"message: '{answer.answer_label}', value:'{answer.answer_id}'"
                    currentAnsw = '{'+ currentAnsw + '}'
                    listAnswersStart = listAnswersStart + currentAnsw + ', '
            listAnswersStart = listAnswersStart[:-2]
            listAnswersStart = listAnswersStart + '\n'
            main_options = 'var options_list = ' + '[\n' + listAnswersStart + ']\n'
    return (main_options)

def templateCreator(questions, labels, answers, dynamic):
    codeLogicStart = 'var dynamicKeysMap = ionSystem.newEmptyStruct(); \n for (var i = 0; i < auto_answer_question_list.length; i++){ \n for (var j = 0; j < auto_answer_question_list[i].length; j++) {\n var auto_answer_result = document.get(auto_answer_question_list[i][j]["varname"] + "_auto_answer_result").toString(); \n var filteredOptions = options_list[i].filter(function (option) {\n return auto_answer_result.indexOf(option["value"]) != -1;});\n var is_auto_answered = true;\n if (filteredOptions.length == 0){\n is_auto_answered = false;\n filteredOptions = options_list[i];\n} \n var inputProperties = ionSystem.newEmptyList();\n inputProperties.add(ionSystem.newString("BUTTON_SELECT"));\n var inputOptions = ionSystem.newEmptyList();\n for (var k = 0; k < filteredOptions.length; k++) {\n var option = ionSystem.newEmptyStruct();\n  option.put("message").newString(filteredOptions[k]["message"]);\n option.put("value").newString(filteredOptions[k]["value"]);\n inputOptions.add(option);\n}\n  var dynamicKeysInput = ionSystem.newEmptyStruct()\n dynamicKeysInput.put("label").newString(auto_answer_question_label_list[i]);\n  dynamicKeysInput.put("type").newString("select_one");\n dynamicKeysInput.put("order").newInt(auto_answer_question_list[i][j]["order"]);\n dynamicKeysInput.put("properties", inputProperties);\n dynamicKeysInput.put("options", inputOptions); \n if(auto_answer_question_list[i][j]["category"] == "fup") {\n dynamicKeysInput.put("conditionalShowExpression").newString(auto_answer_question_list[i][j]["showExpression"]) \n }\n  if(is_auto_answered){ dynamicKeysInput.put("supplemental_info").newString("This is an auto-answered question, please select the option.") \n}\n dynamicKeysMap.put(auto_answer_question_list[i][j]["varname"], \n dynamicKeysInput); }} \n var retVal = ionSystem.newEmptyStruct();\n '
    codeLogincEnd = f'retVal.put("{dynamic}" + "_dynamic_keys", dynamicKeysMap);\n retVal;'
    codeLogic = codeLogicStart + codeLogincEnd
    template = questions + labels + answers + codeLogic
    return (template)    

def dataAnalysis(postInputs):    
    key_name_expression = 'expression-input-'
    key_name_order = 'order-input-'
    ids_to_call = []
    showExpressions = []
    order = []
    dynamic_key_name = postInputs['dynamic-key-name']      
    for keyOrder in postInputs:
        if keyOrder.startswith(key_name_order) == True:
            option = keyOrder.split('input-', 1)[1]
            ids_to_call.append(option)
            order.append(postInputs[keyOrder])            

    for ids in ids_to_call:
        for qID in question_ids_table:
            if ids == qID.question_id:
                print("--IDs")
                print(ids)
                if qID.question_category == 'fup':
                    for inputs in postInputs:
                        if inputs.startswith(key_name_expression):
                            verifVal = inputs.split('input-', 1)[1]
                            if verifVal == ids:                                
                                showExpressions.append(postInputs[inputs])
                else:
                    showExpressions.append("noExpression")
    print("--showExpression list--")
    print(showExpressions)
    question_list_template = genQuestionList(ids_to_call, showExpressions, order)
    labels_list = labels(ids_to_call)
    answers_list = answersGroup(ids_to_call)
    template = templateCreator(question_list_template, labels_list, answers_list, dynamic_key_name)
    return(template)               
