from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia 
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

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

def nova_imagem(request):
    
    # Verificando se o usuario esta logado
    if not request.user.is_authenticated:
        messages.error(request, 'Usúario não está logado!')
        return redirect('login')
    
    # Se estiver logado sera criado um form de acordo com fotografiaForms
    form = FotografiaForms
    
    # Se o method for POST, ou seja estiver passando informações sera criado o form com as informacoes passadas pelo POST
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia cadastrada!')
            return redirect('index')    
    return render(request, 'galeria/nova_imagem.html', {'form':form})

# A funcao recebe o request e o uma outra variavel que sera o id da foto a ser editada
def editar_imagem(request, foto_id):
    # A linha abaixo utiliza o modelo Fotografia para recuperar um objeto de fotografia do banco de dados com base no ID fornecido (foto_id).
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    # Abaixo será verificado se está recebendo alguma informação, se sim será feito um novo form
    # Assim, será feito um novo form a partir de FotografiaForms e o que não for mudado continuara igual (instance=fotografia)
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})