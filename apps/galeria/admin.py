from django.contrib import admin
from apps.galeria.models import Fotografia

class ListarFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('nome', ) # Como deve ser uma tupla, basta colocar ',' no final    
    search_fields = ('nome', ) # Como deve ser uma tupla, basta colocar ',' no final
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicada', )
    list_per_page = 10
    
        
admin.site.register(Fotografia, ListarFotografias)
