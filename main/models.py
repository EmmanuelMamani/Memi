from django.db import models

# Create your models here.

    
class Usuarios(models.Model):
    name=models.CharField(max_length=150)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Eventos(models.Model):
    descripcion_evento=models.CharField(max_length=250)
    imagen_evento=models.CharField(max_length=100)
    costo=models.DecimalField(max_digits=3,decimal_places=2)
    usuario_evento=models.ManyToManyField("Usuarios")
    def __str__(self):
        return self.descripcion_evento
    
class Roles(models.Model):
    name_rol=models.CharField(max_length=100)
    usuario_rol=models.ManyToManyField("Usuarios")
    def __str__(self):
        return self.name_rol

class Cursos(models.Model):
    name_curso=models.CharField(max_length=150)
    descripcion_curso=models.CharField(max_length=250)
    duracion_curso=models.TimeField
    costo_curso=models.DecimalField(max_digits=3,decimal_places=2)
    imagen_curso=models.CharField(max_length=250)
    usuario_curso=models.ManyToManyField("Usuarios")
    def __str__(self):
        return self.name_curso

class Avisos(models.Model):
    descripción_aviso=models.CharField(max_length=250)
    imagen_aviso=models.CharField(max_length=250)
    def __str__(self):
        return self.descripción_aviso
    
class Recursos(models.Model):
    name_recurso=models.CharField(max_length=250)
    link_recurso=models.CharField(max_length=250,default="")
    def __str__(self):
        return self.name_recurso

class Categorias(models.Model):
    name_categoria=models.CharField(max_length=250)
    def __str__(self):
        return self.name_categoria