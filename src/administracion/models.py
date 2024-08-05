from django.db import models
from django.db.models import CASCADE


class Autor(models.Model):
    nombre_completo = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre_completo


class Libro(models.Model):

    CATEGORIAS = (
        (0, "No definido"),
        (1, "Romance"),
        (2, "Terror")
    )

    nombre = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=CASCADE)
    fecha_publicacion = models.DateField(verbose_name="Fecha publicación")
    categoria = models.SmallIntegerField(choices=CATEGORIAS, default=0)


    def __str__(self):
        return "%s - %s" % (self.nombre, self.autor.nombre_completo)

