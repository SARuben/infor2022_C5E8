from django import forms
from .models import Comentario


class comentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        # fields = ('dni','apellido','nombre','email','telefono','textoComentario',)
        fields = '__all__'