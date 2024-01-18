from django.urls import path
from apps.galeria.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('imagem/<int:foto_id>', Imagem, name='imagem'),
    path('buscar', Buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    
    # O caminho que será passado para a view será o editar-imagem/id da foto
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),

]

