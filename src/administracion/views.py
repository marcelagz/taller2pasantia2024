from django.shortcuts import render

from administracion.models import Libro


def inicio(request):
    libros = Libro.objects.all()
    return render(request, "administracion/administracion.html", {"libros": libros})
