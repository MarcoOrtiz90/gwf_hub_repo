from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    context = {'question_ids_table': question_ids_table}
    return render(request, "generator.html", context)