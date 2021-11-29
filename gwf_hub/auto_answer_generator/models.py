from django.db import models
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE

# Create your models here.
class AutoAnswerQuestionTable(models.Model):
    question_id = models.CharField(max_length=50)
    ruleset = models.CharField(max_length=50)
    question_category = models.CharField(max_length=8, null=True)
    question_label = models.TextField()

    def __str__(self):
        return self.question_id

class AutoAnswersTable(models.Model):
    answer_id = models.CharField(max_length=50)
    answer_label = models.CharField(max_length=50)
    parent_question = models.ForeignKey(AutoAnswerQuestionTable, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer_id
