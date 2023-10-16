from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from download.utils import *
from download.main import *
from django.http import HttpResponseRedirect
from vyvod.models import *
from download.models import *

def load_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        test = Test(name=uploaded_file.name).save()
        print(f'media/{PKL.objects.latest("id")}', f'media/{uploaded_file.name}', f'media/{User.objects.latest("id").name}')
        y_real, y_pred = predict(f'media/{PKL.objects.latest("id").pkl}', f'media/{uploaded_file.name}', f'media/{User.objects.latest("id").name}')
        print(y_real, y_pred)
        return HttpResponseRedirect("/")
    return render(request, 'load.html')
