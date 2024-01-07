from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('imagem/<int:foto_id>', Imagem, name='imagem')
]
