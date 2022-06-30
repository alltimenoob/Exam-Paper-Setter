from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
import os
from .models import FilesUpload


def getFile(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'index.html', c)


def getODT(request):
    file = request.FILES['file']
    file.name = request.POST.get("name")+".pdf"
    document = FilesUpload.objects.create(file=file)
    document.save()
    os.system(
        "soffice --infilter=\"writer_pdf_import\" --convert-to odf:\"writer8\" "+file.name)
    response = HttpResponse("Done")
    return response
