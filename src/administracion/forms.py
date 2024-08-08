from django import forms

from administracion.models import Libro, Autor


class FormularioAutor(forms.Form):
    nombre_completo = forms.CharField(required=True, label="Nombre", widget=forms.TextInput(attrs={"class":"formulario"}))

class FormularioLibro(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"formulario"}))
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=True)
    fecha_publicacion = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={"type":"date"}))
    categoria = forms.ChoiceField(choices=Libro.CATEGORIAS, initial=Libro.CATEGORIAS[1])


class FormularioLibroModelo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].initial = "Luis"
        self.fields["autor"].queryset = Autor.objects.filter(nombre_completo__icontains="will")
        self.fields["nombre"].require=True
        #self.fields["categoria"].initial = 2


    class Meta:
        model = Libro
        fields ="__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"formulario"}),
            "fecha_publicacion": forms.DateInput()
        }