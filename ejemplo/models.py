from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                  default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comentario(models.Model):
    dni = models.IntegerField(blank=True, null=True)
    apellido = models.CharField(max_length=50,blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    textoComentario = models.TextField(blank=False, null=False)
    fechaComentario = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + ' '  + self.apellido

    def guardar(self):
        self.fechaComentario = timezone.now()
        self.save()  
          
# Create your models 
# here.
