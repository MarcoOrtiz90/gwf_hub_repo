from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    answers_ids_table = AutoAnswersTable.objects.all()
    if request.method == "POST":
        if request.POST.get('request'):
            input_ids = request.POST.getlist('question_ids', '')
            # for id in question_ids_table:
            #     print(id.question_id)
            #     print(id.question_category)

            fups = []
            mandates = []
            order = len(input_ids)
            for input in input_ids:
                for id in question_ids_table:
                    if input == id.question_id :
                        if id.question_category == "fup":
                            fups.append(input)
                        else:
                            mandates.append(input)
                        
            second_context = {
                    'question_ids_table': question_ids_table,
                    'prevSelect': input_ids,
                    'fups': fups,
                    'mandates': mandates,
                    'order': order
            }
            return render(request, 'generator.html', second_context)

        if request.POST.get('generate'):
            # order_inputs = request.POST.get('')
            # expression_inputs = request.POST.get('')
            # 
            key_name = 'expression-input-'            
            input_ids_generate = request.POST
            for key in input_ids_generate:
                if key.startswith(key_name) == True:
                    option = key.split('input-', 1)[1] 
                    print(option)
            print(input_ids_generate)


    first_context = {'question_ids_table': question_ids_table}
    return render(request, "generator.html", first_context)

    