# Generated by Django 3.2.9 on 2021-11-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoAnswerQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.TextField()),
                ('ruleset', models.TextField()),
                ('question_label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AutoAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.TextField()),
                ('answer_label', models.TextField()),
            ],
        ),
    ]
