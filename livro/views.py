from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from livro.models import Livros
from livro.models import Categoria
import requests
import pandas as pd
import json
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
       

        return render(request, 'home.html', {'livros':livros,
                                            'usuario_logado':request.session.get('usuario'),
                                            'form':form})
        
    else:
        return redirect ('/auth/login/?status=2')


def consulta_livro(request, id):
    livros = Livros.objects.get(id = id)
    form = CadastroLivro()
    return render(request, 'consulta_livro.html',{'livro':livros,
                                                'usuario_logado':request.session.get('usuario'),
                                                'form':form,
                                                'id_livro':id})


def cadastra_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        
        
        if form.is_valid():
            form.save()
            return redirect('livro/home')
        else:
            return HttpResponse('DADOS INVALIDOS')


def devolver_livro(request,id):
    livro=Livros.objects.get(id=id).delete()
    return redirect('/livro/home')












