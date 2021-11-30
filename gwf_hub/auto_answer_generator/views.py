from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    if request.method == "POST":
        context2 = request.POST.getlist('question_ids', '')
        content = {
                'question_ids_table': question_ids_table,
                'prevSelect': context2
        }
        print(content)
        print("second")
        return render(request, 'generator.html', content)

    context = {'question_ids_table': question_ids_table}
    print(context)
    print("first")
    return render(request, "generator.html", context)

    