from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('venta/crear/', views.crear_venta, name='crear_venta'),
    path('reporte_existencias/', views.reporte_existencias, name='reporte_existencias'),
    path('reporte_ventas/', views.reporte_ventas, name='reporte_ventas'),
]
