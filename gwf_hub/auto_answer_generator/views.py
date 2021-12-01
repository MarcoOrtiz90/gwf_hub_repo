from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    if request.method == "POST":
        contextTwo = request.POST.getlist('question_ids', '')
        content = {
                'question_ids_table': question_ids_table,
                'prevSelect': contextTwo
        }
        for id in question_ids_table:
            print(id.question_id)
            print(id.question_category)

        fups = []
        for input in contextTwo:
            for id in question_ids_table:
                if input == id and id.question_ids_table == "fup":
                    print("hello")
        
        # print(context2)
        print("second")
        return render(request, 'generator.html', content)

    context = {'question_ids_table': question_ids_table}
    print(context)
    print("first")
    return render(request, "generator.html", context)

    