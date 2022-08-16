from django.shortcuts import render, redirect
import datetime 
from ejemplo.models import Noticia , Comentario, Video, Historia
from django.views.generic import DetailView,ListView,CreateView,DeleteView,UpdateView
from django.conf import settings 
from django.core.mail import send_mail
from .form import NoticiasForm, comentarioForm
from django.urls import reverse_lazy


# Create your views here

class Inicio(ListView):
  model = Noticia
  form_class = NoticiasForm
  template_name = 'inicio.html'
  paginate_by  = 3

  def get_queryset(self): 
        query = super(Inicio,self).get_queryset().order_by('-published_date').values()
        return query

def contacto(request):
    return render(request,'FormularioContacto.html')

class Videos(ListView):
   model = Video
   template_name = 'videos.html'
   
   def  get_queryset(self):
        query = super(Videos,self).get_queryset
        return query 


def calendario(request):    
    return render(request,'calendario.html')

def contactar(request):
    if request.method == 'POST':
          asunto = request.POST["txtAsunto"]
          mensaje = request.POST["txtMensaje"] + "/Email:" + request.POST["txtEmail"]
          email_desde = settings.EMAIL_HOST_USER
          email_para = ["arubensanchezg@gmail.com"]
          send_mail(asunto,mensaje,email_desde,email_para,fail_silently=False) 
          return render(request,'envioexitoso.html')
    return render(request,'FormularioContacto.html')      

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


