from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
   

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    data_cadastro = models.DateField (default = date.today)
    emprestado = models.BooleanField(default = False, blank = True, null = True)
    usuario_emprestado = models.CharField(max_length=30, blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Livro'