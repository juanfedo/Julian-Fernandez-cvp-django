from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(default=timezone.now)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} vendidos en {self.fecha_venta}"