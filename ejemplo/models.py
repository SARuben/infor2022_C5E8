from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.utils import timezone
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

class Noticia(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                  default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    imagen = models.ImageField(upload_to = 'imagenes/',null=True,blank=True)    
    
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
        

class Video(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    url = URLField(null=True)
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField()

class  Historia(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    historia = models.TextField()
    imagen = models.ImageField(upload_to = 'imagenes/', null=True, blank=True)   
    
 # Create your models 
# here.
