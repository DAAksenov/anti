from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from download.utils import *
from download.main import *
from django.http import HttpResponseRedirect

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        model_name = fit(uploaded_file.name)
        
        # Тут будет Пашина хуйня

        return HttpResponseRedirect("/")
    return render(request, 'upload.html')
