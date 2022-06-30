from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
import os
from django.core.files.storage import default_storage


def getFile(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'index.html', c)


def getODT(request):
    file = request.FILES['file']
    file.name = request.POST.get("name")+".pdf"
    file_name = default_storage.save(file.name, file)

    os.system(
        "soffice --infilter=\"writer_pdf_import\" --convert-to odf:\"writer8\" "+file_name)

    file = default_storage.open(file_name)

    response = HttpResponse(file, content_type='application/odt')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response
