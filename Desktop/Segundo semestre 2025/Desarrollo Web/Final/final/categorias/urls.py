from django.urls import path
from .views import lista_categorias, agregar_categoria, editar_categoria

urlpatterns = [
    path('', lista_categorias, name='lista_categorias'),
    path('agregar/', agregar_categoria, name='agregar_categoria'),
    path('editar/<int:id>/', editar_categoria, name='editar_categoria'),
]
