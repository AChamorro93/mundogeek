from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=120, unique=True)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    telefono = models.CharField(max_length=10)  

    def save(self, *args, **kwargs):
        if not self.pk or Usuario.objects.filter(pk=self.pk, password=self.password).exists():
            self.password = make_password(self.password)
        super().save(*args, **kwargs) #HACE EL HASHEO 

    def check_password(self, raw_password):
        return check_password(raw_password, self.password) #VERIFICA PASSWORD

    def __str__(self):
        return self.nombre_usuario

class Producto(models.Model):
    name = models.CharField(max_length=120)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    tecnologia = models.CharField(max_length=50)
    descrip = models.CharField(max_length=1000)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name  


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    foto = models.ImageField(upload_to='producto/')

    def __str__(self):
        return f"Imagen de {self.producto.name}"


