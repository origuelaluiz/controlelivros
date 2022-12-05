from django.urls import path
from livro import views 

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('consulta_livro/<int:id>', views.consulta_livro, name = 'consulta_livro'),
    path('cadastra_livro', views.cadastra_livro, name = 'cadastra_livro'),
    path('devolver_livro/<int:id>', views.devolver_livro, name = 'devolver_livro'),
    
    
]