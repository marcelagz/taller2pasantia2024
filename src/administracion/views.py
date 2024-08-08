from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from administracion.models import Autor
from .forms import FormularioLibro, FormularioAutor, FormularioLibroModelo
from .models import Libro


def inicio(request):
    form = FormularioAutor()
    libros = Libro.objects.all()
    #form_libro = FormularioLibro()
    form_libro = FormularioLibroModelo(initial={"categoria":1})
    return render(request, "administracion/administracion.html", context={"libros": libros,
                                                                          "form":form, "form_libro":form_libro})

def crear(request):
    form = FormularioLibro()

    if request.method == "POST":
        form = FormularioLibro(request.POST)

        if form.is_valid():
            Libro.objects.create(nombre=form.cleaned_data["nombre"], autor=form.cleaned_data["autor"],
                                 fecha_publicacion=form.cleaned_data["fecha_publicacion"], categoria=form.cleaned_data["categoria"])
            return redirect("index")


    return render(request, template_name="administracion/creacion.html",context={"form":form})

def crear_libro_modelo(request):
    form = FormularioLibroModelo()

    if request.method == "POST":
        form = FormularioLibroModelo(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, template_name="administracion/creacion.html", context={"form": form})

def editar_libro_modelo(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = FormularioLibroModelo(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado Exitosamente")
            return redirect("index")
        else:
            messages.error(request,form.errors)

    return render(request, template_name="administracion/editar_libro.html", context={"form": FormularioLibroModelo(instance=libro)})

