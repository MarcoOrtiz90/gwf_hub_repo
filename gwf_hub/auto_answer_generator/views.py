from django.shortcuts import render
from .models import AutoAnswerQuestionTable, AutoAnswersTable

# Create your views here.
def aaGenerator(request):
    question_ids_table = AutoAnswerQuestionTable.objects.all()
    context = {'question_ids_table': question_ids_table}
    
    if request.method == "POST":
        if request.POST.get("new-id"):
            pass
        elif request.POST.get("request"):
            if request.htmx:
                content = request.POST.getlist('question_ids', '')
                print(content[1])
                return render(request, 'generator-form.html', context)
    
    return render(request, "generator.html", context)