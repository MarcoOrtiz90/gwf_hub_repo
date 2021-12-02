from django.shortcuts import render
from . import functions
import pandas as pd
from . import albacorizer_main
import openpyxl
from .forms import UploadFileForm

def load_albacorizer(request):
    return render(request, 'albacorizer.html')


def jsoncodes(request):
    if request.method == 'POST':
        source_file = request.FILES["sourcefile"]
        # wb = openpyxl.load_workbook(source_file)
        data_dict = albacorizer_main.new_ms_albacorize(source_file)
        # df_ms_questions = pd.read_excel(wb, sheet_name='master sheet')
        # questions_json = functions.question_answer_build(df_ms_questions)
        # df_ms_sections = pd.read_excel(wb, sheet_name='master sheet')
        # df_wid = pd.read_excel(wb, sheet_name='widget ids')
        # sections_json = functions.section_build(df_ms_sections, df_wid)
        return render(request, 'albacorizer_output.html', data_dict)
