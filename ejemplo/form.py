from django import forms
from .models import Comentario, Noticia
from .models import Noticia


class comentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        # fields = ('dni','apellido','nombre','email','telefono','textoComentario',)
        fields = '__all__'

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
