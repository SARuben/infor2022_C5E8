from django.contrib import admin
from .models import GaleriaFoto, Historia, Noticia, Video, Equipo
from .models import Comentario
admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Video)
admin.site.register(Historia)
admin.site.register(Equipo)
admin.site.register(GaleriaFoto)
# Register your models here.
