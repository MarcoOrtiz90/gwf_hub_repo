from django.contrib import admin

# Register your models here.
from .models import AutoAnswerQuestionTable
from .models import AutoAnswersTable

admin.site.register(AutoAnswerQuestionTable)
admin.site.register(AutoAnswersTable)