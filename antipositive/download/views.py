from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from download.utils import *
from download.main import *
from django.http import HttpResponseRedirect
from download.models import *

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        user = User(name=uploaded_file.name).save()
        model_name = fit(f"media/{uploaded_file.name}")
        pkl = PKL(pkl=model_name).save()
        # Тут будет Пашина хуйня

        return HttpResponseRedirect("/")
    return render(request, 'upload.html')
