from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from categorias.models import Categoria

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def agregar_producto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            precio=request.POST['precio'],
            descripcion=request.POST['descripcion'],
            categoria_id=request.POST['categoria'],
            stock=request.POST['stock']
        )
        return redirect('lista_productos')
    return render(request, 'productos/agregar.html', {'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio'],
        producto.descripcion = request.POST['descripcion'],
        producto.categoria_id = request.POST['categoria'],
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('lista_productos')
    return render(request, 'productos/editar.html', {'producto': producto, 'categorias': categorias})
