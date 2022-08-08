from ast import Try
from xml.dom import ValidationErr
from django.db import models
from django.db.models import F
from django.core.validators import MinValueValidator
from django.forms import ValidationError

# Create your models here.

class Componentes(models.Model):
    tipos = (
        ('Raton', 'Raton'),
        ('Teclado', 'Teclado'),
        ('Monitor', 'Monitor'),
        ('Altavoz', 'Altavoz'),
        ('Procesador', 'Procesador'),
        ('Placa', 'Placa')
    )
    tipo = models.CharField(max_length=50, choices=tipos)
    
    class Meta:
        abstract = True
        
class DispositivosEntrada (Componentes):
    marca = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    
class DispositivosSalida(Componentes):
    marca = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        
class DispositivosInterno(Componentes):
    marca = models.CharField(max_length=50)
    
    class Meta:
        abstract = True

class Raton(DispositivosEntrada):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
  
    def __str__(self):
        return f'{self.tipo} - {self.marca}'
  
class Teclado(DispositivosEntrada):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'

class Monitor(DispositivosSalida):
    tamaño = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.tamaño}'

class Altavoz(DispositivosSalida):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'
    
class Procesador(DispositivosInterno):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'
    
class Placa(DispositivosInterno):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'

class Computadora(models.Model):
    nombre = models.CharField(max_length=50)
    raton = models.ForeignKey(Raton, on_delete=models.CASCADE)
    teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    altavoz = models.ForeignKey(Altavoz, on_delete=models.CASCADE)
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    placa = models.ForeignKey(Placa, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    costo = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return f'{self.nombre}'
    
    def componentes(self):
        raton  = Raton.objects.filter(id=self.raton.id)
        teclado  = Teclado.objects.filter(id=self.teclado.id)
        monitor  = Monitor.objects.filter(id=self.monitor.id)
        altavoz  = Altavoz.objects.filter(id=self.altavoz.id)
        procesador  = Procesador.objects.filter(id=self.procesador.id)
        placa  = Placa.objects.filter(id=self.placa.id)
        
        componentes = (raton, teclado, monitor, altavoz, procesador, placa)
        
        return componentes
    
    def verificar_stock(self):
        componentes = self.componentes()
        mensaje =''
        for componente in componentes:
            if componente[0].cantidad < self.cantidad:
                mensaje += componente[0].tipo + ', '
                
        return mensaje
    
    def decrementar_cantidad(self):
        mensaje = self.verificar_stock()
        componentes = self.componentes()
        total = 0    
    
        if len(mensaje)==0:
            for componente in componentes:
                componente.update(cantidad = F('cantidad') - self.cantidad)
                total += componente[0].costo
                
        return {
            'mensaje': mensaje,
            'total': total
        }
        
    def save(self, *args, **kwargs):
        resultado = self.decrementar_cantidad()
        
        # print(resultado['mensaje'])
        # print(resultado['total'])
        
        if resultado['total'] > 0:
            self.costo = resultado['total']
            super(Computadora,self).save(*args, **kwargs)
        else:
            raise ValidationError(resultado['mensaje'] + ' no tiene stock suficiente')
        

class Orden(models.Model):
    costo_orden = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)    
    
    def __str__(self):
        return f'{self.id}'
    
class DetalleOrden(models.Model):
    cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.orden} - {self.computadora}'
    
    
    def save(self, *args, **kwargs):
        
        computadora  = Computadora.objects.filter(id=self.computadora.id)
        orden = Orden.objects.filter(id=self.orden.id)
        
        resultado = self.decrementar_cantidad()
        
        if computadora[0].cantiad >= self.cantidad:
            computadora.update(cantidad = F('cantidad') - self.cantidad)
            
            
        
        if resultado['total'] > 0:
            self.costo = resultado['total']
            super(Computadora,self).save(*args, **kwargs)
        else:
            raise ValidationError(resultado['mensaje'] + ' no tiene stock suficiente')
    
    
    
    
    

            
# class Orden(models.Model):
#     nombre = models.CharField(max_length=50)
#     cantidad = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
#     computadoras = models.ManyToManyField(Computadora)
      
#     def __str__(self):
#         return f'{self.nombre}'
    
    
    
# monitor = Monitor.objects.filter(id=self.monitor.id)
#         teclado  = Teclado.objects.filter(id=self.teclado.id)
#         raton  = Raton.objects.filter(id=self.teclado.id)
#         print(monitor[0].contador)
#         print(teclado[0].contador)
#         print(raton[0].contador)
        
#         if (monitor[0].contador >= self.contador and 
#             teclado[0].contador >= self.contador and 
#             raton[0].contador >= self.contador ):
#             monitor.update(contador = F('contador')- self.contador)
#             teclado.update(contador = F('contador')- self.contador)
#             raton.update(contador = F('contador')- self.contador)
#             super(Computadora,self).save(*args, **kwargs)
#         else:
#             return False

# raton  = Raton.objects.filter(id=self.raton.id)
        # raton1  = Raton.objects.filter(id=self.raton.id).get().cantidad
        # teclado  = Teclado.objects.filter(id=self.teclado.id)
        # monitor  = Monitor.objects.filter(id=self.monitor.id)
        # altavoz  = Altavoz.objects.filter(id=self.altavoz.id)
        # procesador  = Procesador.objects.filter(id=self.procesador.id)
        # placa  = Placa.objects.filter(id=self.placa.id)
        
        # print(raton1)
        
        # if raton[0].cantidad >= self.cantidad and teclado[0].cantidad >= self.cantidad and monitor[0].cantidad >= self.cantidad and altavoz[0].cantidad >= self.cantidad and procesador[0].cantidad >= self.cantidad and placa[0].cantidad >= self.cantidad:
        #     """Decremento de la existencia"""
        #     raton.update(cantidad = F('cantidad') - self.cantidad)
        #     teclado.update(cantidad = F('cantidad') - self.cantidad)
        #     monitor.update(cantidad = F('cantidad') - self.cantidad)
        #     altavoz.update(cantidad = F('cantidad') - self.cantidad)
        #     procesador.update(cantidad = F('cantidad') - self.cantidad)
        #     placa.update(cantidad = F('cantidad') - self.cantidad)
            
        #     total = raton[0].costo + teclado[0].costo+ monitor[0].costo +altavoz[0].costo + procesador[0].costo + placa[0].costo
            
        #     return total
        # else:
        #     return 0