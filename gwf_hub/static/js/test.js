var auto_answer_question_label_list = [[{'var': 'Q-sa-age', 'category': 'fup', 'showExpression': 'eval(oip_captured) === True', 'order': '2'}], [{'var': 'Q-pmt-age-cc', 'category': 'fup', 'showExpression': 'eval(gsi_attrb) === False', 'order': '3'}]] var auto_answer_question_label_list = ['Is the SA new?', 'What is the age of the payment?'] var options_list = [[{'message': 'New Address', 'value': 'A-sa-age-new'}, {'message': 'Old Address', 'value': 'A-sa-age-old'}], [{'message': 'Old Card', 'value': 'A-pmt-card-old'}, {'message': 'New Card', 'value': 'A-pmt-card-new'}]]  var dynamicKeysMap = ionSystem.newEmptyStruct(); for (var i = 0; i < auto_answer_question_list.length; i++){for (var j = 0; j < auto_answer_question_list[i].length; j++) {var auto_answer_result = document.get(auto_answer_question_list[i][j]["varname"] + "_auto_answer_result").toString(); var filteredOptions = options_list[i].filter(function (option) {return auto_answer_result.indexOf(option["value"]) != -1;}); var is_auto_answered = true; if (filteredOptions.length == 0){ is_auto_answered = false; filteredOptions = options_list[i];} var inputProperties = ionSystem.newEmptyList(); inputProperties.add(ionSystem.newString("BUTTON_SELECT")); var inputOptions = ionSystem.newEmptyList(); for (var k = 0; k < filteredOptions.length; k++) { var option = ionSystem.newEmptyStruct();  option.put("message").newString(filteredOptions[k]["message"]); option.put("value").newString(filteredOptions[k]["value"]); inputOptions.add(option);}  var dynamicKeysInput = ionSystem.newEmptyStruct() dynamicKeysInput.put("label").newString(auto_answer_question_label_list[i]);  dynamicKeysInput.put("type").newString("select_one");            dynamicKeysInput.put("order").newInt(auto_answer_question_list[i][j]["order"]); dynamicKeysInput.put("properties", inputProperties); dynamicKeysInput.put("options", inputOptions); if(auto_answer_question_list[i][j]["category"] == "fup") { dynamicKeysInput.put("conditionalShowExpression").newString(auto_answer_question_list[i][j]["showExpression"]) } if(is_auto_answered){ dynamicKeysInput.put("supplemental_info").newString("This is an auto-answered question, please select the option.") }  dynamicKeysMap.put(auto_answer_question_list[i][j]["varname"], dynamicKeysInput); }} var retVal = ionSystem.newEmptyStruct(); retVal.put("gsi_attr" + "_dynamic_keys", dynamicKeysMap); retVal; 