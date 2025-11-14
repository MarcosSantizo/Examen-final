from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion']
        )
        return redirect('lista_categorias')
    return render(request, 'categorias/agregar.html')

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.descripcion = request.POST['descripcion']
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'categorias/editar.html', {'categoria': categoria})
