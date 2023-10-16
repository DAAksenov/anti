from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
from download.utils import *
from download.main import *
from django.http import HttpResponseRedirect
from vyvod.models import *
from download.models import *
from vyvod.utils import *
import pandas as pd
import numpy as np
import json
from django.core.paginator import Paginator

def load_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        test = Test(name=uploaded_file.name).save()
        y_real, y_pred = predict(f'media/{PKL.objects.latest("id").pkl}', f'media/{uploaded_file.name}', f'media/{User.objects.latest("id").name}')
        array1 = convert_array(y_real)
        rounded_array = round_array(y_pred)
        array2 = convert_array2(rounded_array)
        Data(array1=array1, array2=array2).save()
        return redirect("/test/res")
    return render(request, 'load.html')


def data_view(request):
    data = Data.objects.latest('id')
    first = json.loads(data.array1)
    second = json.loads(data.array2)
    df = pd.DataFrame.from_records({'Исходные данные': first, 'Предсказанные данные': second})
    print(df)

    p = Paginator(df, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'df': df, 'page_obj': page_obj}
    return render(request, 'data.html', context)
