from django.db import models

class Autos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

class Camionetas(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Camioneta"
        verbose_name_plural = "Camionetas"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}"  
    
class Motos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}" 