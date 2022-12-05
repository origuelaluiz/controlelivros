from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1') #NOME E EMAIL EM BRANCO

    if len(senha) < 8:
        return redirect ('/auth/cadastro/?status=2') #SE A SENHA É CURTA OU NÃO

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')  #VERIFICA SE O USUARIO JÁ É EXISTENTE NO SITEMA

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, senha = senha, email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0') #CONECTADO COM SUCESSO
    except:
        return redirect('/auth/cadastro/?status=4') #ERRO DE CONEXÃO DO SISTEMA


def valida_login(request):
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home')

    return HttpResponse(f"{email} {senha}")

def logout(request):
    request.session.flush()
    return redirect ('/auth/login/')

