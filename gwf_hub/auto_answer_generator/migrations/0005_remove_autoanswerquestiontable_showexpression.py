# Generated by Django 3.2.9 on 2021-11-29 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_answer_generator', '0004_auto_20211129_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoanswerquestiontable',
            name='showExpression',
        ),
    ]