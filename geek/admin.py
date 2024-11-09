from django.contrib import admin
from .models import Producto, Usuario, Imagen

from django.contrib import admin
from .models import Producto, Imagen

class ImagenInline(admin.TabularInline): #me va a permitir cargar may imagenes para el mismo producto
    model = Imagen
    extra = 1  # Muestra un campo de imagen adicional vacío

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenInline]   # gestiona las imagenes del producto


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario)
