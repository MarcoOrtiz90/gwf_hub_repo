from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable
from . import generator

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    answers_ids_table = AutoAnswersTable.objects.all()
    if request.method == "POST":
        if request.POST.get('request'):
            input_ids = request.POST.getlist('question_ids', '')
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
            input_ids_generate = request.POST
            template = generator.dataAnalysis(input_ids_generate)
            print("===FINAL TEMPLATE==")
            print(template)
            print(type(template))
            third_context = {
                'prevSelect': [],
                'generated': template
            }
            return render(request, 'generator.html', third_context)
            


    first_context = {'question_ids_table': question_ids_table}
    return render(request, "generator.html", first_context)

    