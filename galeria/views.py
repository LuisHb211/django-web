from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return render(request, 'galeria/index.html')

def Imagem(request):
    return render(request, 'galeria/imagem.html')