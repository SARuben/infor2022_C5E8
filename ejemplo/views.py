from django.shortcuts import render, redirect
import datetime 
from ejemplo.models import GaleriaFoto, Noticia , Comentario, Video, Historia,Equipo
from django.views.generic import DetailView,ListView,CreateView,DeleteView,UpdateView
from django.conf import settings 
from .form import NoticiasForm, comentarioForm, fotoForm, CustomUserCreationForm 
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login  
from django.contrib import messages



# Create your views here

class Inicio(ListView):
  model = Noticia
  form_class = NoticiasForm
  template_name = 'inicio.html'
  paginate_by  = 3

  def get_queryset(self): 
        query = super(Inicio,self).get_queryset().order_by('-published_date').values()
        return query

class Videos(ListView):
   model = Video
   template_name = 'videos.html'
   
   def  get_queryset(self):
        query = super(Videos,self).get_queryset
        return query 


def calendario(request):    
    return render(request,'calendario.html')

class CrearComentario(CreateView):
    model = Comentario
    form_class  = comentarioForm
    template_name = 'CrearComentario.html'
    success_url = reverse_lazy('inicio')

class Historias(ListView):
    model = Historia
    template_name = 'GaleriaHistorias.html'
    def  get_queryset(self):
        query = super(Historias,self).get_queryset
        return query 

class Integrantes(ListView):
    model = Equipo
    template_name = 'Equipo.html'

    def get_queryset(self):
        query = super(Integrantes,self).get_queryset
        return query

class Fotos(ListView):
    model = GaleriaFoto
    template_name = 'GaleriaFotos.html'

    def get_queryset(self):
        query = super(Fotos,self).get_queryset
        return query

class MostrarFoto(DetailView):
    model = GaleriaFoto
    form_class = fotoForm
    template_name = 'MostrarUnaFoto.html'

def detalleImagen(request,id):
    imagen = GaleriaFoto.objects.get(id=id)     
    context = {'imagen':imagen}
    return render(request,'VerImagen.html',context)

def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],
                                password = formulario.cleaned_data["password1"])
            messages.success(request,'Te has registrado correctamente')                    
            login(request,user)                    
            # ir al home
            return redirect(to ='inicio')
        

    return render(request,'registration/registro.html',data)




    

        
        



