from django import forms
from .models import AutoAnswerQuestionTable, AutoAnswersTable

class AutoAnswerQuestionTableForm(forms.ModelForm):
    class Meta:
        model = AutoAnswerQuestionTable
        fields = ['question_id', 'ruleset', 'question_category', 'question_label']

class AutoAnswersTableForm(forms.ModelForm):
    class Meta:
        model = AutoAnswersTable
        fields = ['answer_id', 'answer_label', 'parent_question' ]