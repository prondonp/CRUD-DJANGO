# autos/models.py

from django.db import models
import uuid

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

class TipoAuto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.tipo_nombre

class Modelo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre_modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    class Meta:
        unique_together = ('marca', 'nombre_modelo', 'año')

    def __str__(self):
        return f"{self.marca} {self.nombre_modelo} {self.año}"

class TipoCombustible(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_combustible = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.tipo_combustible

class Transmision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_transmision = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.tipo_transmision

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_color = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre_color

class Concesionario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.concesionario})"

class Auto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo_auto = models.ForeignKey(TipoAuto, on_delete=models.CASCADE)
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    transmision = models.ForeignKey(Transmision, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.modelo} ({self.vin})"

class Venta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Venta de {self.auto} a {self.cliente} por {self.vendedor} el {self.fecha_venta}"

class Servicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_servicio = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre_servicio

class AutoServicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_servicio = models.DateTimeField(auto_now_add=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Servicio {self.servicio} para {self.auto} el {self.fecha_servicio}"

class Seguro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proveedor = models.CharField(max_length=100)
    numero_poliza = models.CharField(max_length=50, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_cobertura = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Seguro {self.numero_poliza} por {self.proveedor}"

class AutoSeguro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Seguro {self.seguro} para {self.auto}"

class Garantia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proveedor = models.CharField(max_length=100)
    numero_garantia = models.CharField(max_length=50, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    detalles_cobertura = models.TextField()
    
    def __str__(self):
        return f"Garantía {self.numero_garantia} por {self.proveedor}"

class AutoGarantia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    garantia = models.ForeignKey(Garantia, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Garantía {self.garantia} para {self.auto}"

class RegistroMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Mantenimiento para {self.auto} el {self.fecha_mantenimiento}"

class Reparacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_reparacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.tipo_reparacion

class AutoReparacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    reparacion = models.ForeignKey(Reparacion, on_delete=models.CASCADE)
    fecha_reparacion = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Reparación {self.reparacion} para {self.auto} el {self.fecha_reparacion}"
