from django.urls import path

from administracion.views import inicio, crear, crear_libro_modelo, editar_libro_modelo

urlpatterns = [
    path('', inicio, name="index"),
    path('creacion', crear, name="crear"),
    path('creacion/modelo', crear_libro_modelo, name="crear_modelo"),
    path('editar/libro/<int:pk>', editar_libro_modelo, name="editar_libro")
]