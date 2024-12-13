
from django.contrib import admin
from django.conf import settings
from django.urls import path
from geek import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base_view, name='base'),

    path('menuini/',views.menuini, name='menuini'),

    path('accesorios/', views.accesorios, name='accesorios'),
    path('carrito/', views.ver_carrito, name='carrito'),
    
    path('inisesion/', views.inisesion, name='inisesion'),
    path('registro/', views.UsuarioCreateView.as_view(), name='registro'),
    path('proform/', views.ProductoCreateView.as_view(), name='proform'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('producto/<int:producto_id>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('productos/', views.ProductoListView.as_view(), name='pronue'),

    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),


    
    path('lightper/', views.lightper, name='lightper'),
    path('ligpix/', views.ligpix, name='ligpix'),
    path('ligrgb/', views.ligrgb, name='ligrgb'),
    path('polenvio/', views.polenvio, name='polenvio'),
    path('polgar/', views.polgar, name='polgar'),
    path('polpri/', views.polpri, name='polpri'),
    path('prefre/', views.prefre, name='prefre'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
