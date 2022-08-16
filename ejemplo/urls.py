from django.urls import path
from . import views

urlpatterns = [
    # path('', views.inicio, name='inicio'),
    path('', views.Inicio.as_view(), name='inicio'),
    path('contacto/', views.contacto, name='contacto'),  
    path('contactar/',views.contactar, name='contactar'),
    path('videos/',views.Videos.as_view(), name = 'videos'),
    path('calendario/',views.calendario, name = 'calendario'),
    path('crearcomentario/',views.CrearComentario.as_view(), name='crearcomentario'),
    path('Historias/',views.Historias.as_view(),name='Historias'),
]