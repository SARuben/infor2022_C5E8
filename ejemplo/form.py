from ast import Pass
from django import forms
from .models import Comentario, GaleriaFoto, Noticia
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class comentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        # fields = ('dni','apellido','nombre','email','telefono','textoComentario',)
        fields = '__all__'

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class fotoForm(forms.ModelForm):
    class Meta:
        model = GaleriaFoto 
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']
        

               
