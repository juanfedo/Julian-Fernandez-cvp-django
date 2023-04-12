from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Producto, Venta
from .forms import ProductoForm, VentaForm

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def reporte_existencias(request):
    productos = Producto.objects.all()
    return render(request, 'Inventario/reporte_existencias.html', {'productos': productos})

@login_required
@permission_required('Inventario.crear_producto')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('reporte_existencias')
    else:
        form = ProductoForm()
    return render(request, 'Inventario/crear_producto.html', {'form': form})

@login_required
@permission_required('Inventario.change_producto')
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('reporte_existencias')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Inventario/editar_producto.html', {'form': form, 'producto': producto})

@login_required
@permission_required('Inventario.add_venta')
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)  # obtener instancia del modelo Venta sin guardarla en la BD
            producto = venta.producto
            cantidad_vendida = venta.cantidad
            if cantidad_vendida > producto.cantidad:
                messages.error(request, f'No hay suficientes unidades de {producto.nombre} en inventario')
                return render(request, 'Inventario/crear_venta.html', {'form': form})
            else:
                producto.cantidad -= cantidad_vendida
                producto.save()
                venta.save()
                messages.success(request, 'Venta registrada correctamente.')
                return redirect('reporte_ventas')
    else:
        form = VentaForm()
    return render(request, 'Inventario/crear_venta.html', {'form': form})


@login_required
def reporte_ventas(request):
    ventas = Venta.objects.all()
    for venta in ventas:
        venta.precio_unitario = venta.producto.precio
        venta.total = venta.cantidad * venta.precio_unitario
    return render(request, 'Inventario/reporte_ventas.html', {'ventas': ventas}) 

@login_required
@permission_required('Inventario.delete_producto')
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('reporte_existencias')
    return render(request, 'Inventario/eliminar_producto.html', {'producto': producto})    
