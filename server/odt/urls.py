from os import stat
from pydoc import doc
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.getFile),
    path('getODT/', views.getODT)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
