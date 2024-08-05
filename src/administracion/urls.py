from django.urls import path

from administracion.views import inicio

urlpatterns = [
    path('', inicio, name="index")
]