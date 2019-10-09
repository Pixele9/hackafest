from django.db import models

# Create your models here.
class clientes(models.Model):

    sexos = [
        ('M','Masculino'),
        ('F','Femenino')
    ]

    socio = models.PositiveIntegerField()
    contrato = models.PositiveIntegerField()
    estado = models.ForeignKey('estados', on_delete=models.CASCADE)
    ciudad = models.ForeignKey('municipios', on_delete=models.CASCADE)
    tipo = models.ForeignKey('prestamos', on_delete=models.CASCADE)
    fechaEntrega = models.DateField(auto_now=False, auto_now_add=False)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    diasVencidos = models.PositiveIntegerField()
    abonosVencidos = models.PositiveIntegerField()
    nacimiento =  models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=1, choices=sexos)
    descripcionOcupacion = models.CharField(max_length=50)

class estados(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class municipios(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class prestamos(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)