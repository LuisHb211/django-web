from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('imagem/', Imagem, name='imagem')
]
