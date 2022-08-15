from django.contrib import admin
from .models import Historia, Noticia, Video
from .models import Comentario
admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Video)
admin.site.register(Historia)
# Register your models here.
