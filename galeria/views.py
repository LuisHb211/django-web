from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia 
from django.contrib import messages

def Index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usúario não está logado!')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    return render(request, 'galeria/index.html', {'cards': fotografias})

def Imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def Buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usúario não está logado!')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if "buscar" in request.GET:
        palavra_chave = request.GET["buscar"]
        if palavra_chave:
            fotografias = fotografias.filter(nome__icontains=palavra_chave)
    return render(request, 'galeria/buscar.html', {'cards': fotografias})