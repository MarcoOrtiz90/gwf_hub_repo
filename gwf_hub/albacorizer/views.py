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
        try:
            source_file = request.FILES["sourcefile"]
            source_file_name = str(request.FILES["sourcefile"].name)
            print(source_file_name)
            if source_file_name.endswith('.xlsx') or source_file_name.endswith('.xlsm'):
                data_dict = albacorizer_main.new_ms_albacorize(source_file)
                return render(request, 'albacorizer_output.html', data_dict)
            else:
                data_dict = {"Error": "Incorrect file type, please upload .xlsx or xlsm files."}
                return render(request, 'albacorizer.html', data_dict)
        except Exception as ve:
            print("Value Error noted as - ", ve)
