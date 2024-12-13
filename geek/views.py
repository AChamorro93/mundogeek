from django.contrib import messages  
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import Usuario, Producto
from .forms import RegistroForm, ProductoForm
from django.urls import reverse_lazy

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('menuini') 
    def form_valid(self, form):
        messages.success(self.request,"Usuario registro correctamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"ERROR, favor de verificar que todo este correcto")
        return super().form_invalid(form) 

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'proform.html'
    success_url = reverse_lazy('menuini')

class ProductoListView(ListView):
    model = Producto
    template_name = 'pronue.html'  
    context_object_name = 'productos'  # Se usará 'productos' en el template para acceder a la lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagenes'] = self.object.imagenes.all()  
        context['form'] = ProductoForm()
        return context
    
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    # Recuperar la cantidad desde el formulario, o usar 1 por defecto
    cantidad = int(request.POST.get('cantidad', 1))  # Si no se pasa cantidad, usar 1 como valor predeterminado
    
    # Obtener el carrito desde la sesión
    carrito = request.session.get('carrito', {})

    # Verificar si el producto ya está en el carrito
    if producto.id in carrito:
        # Si el producto ya está en el carrito, sumamos la cantidad
        carrito[producto.id]['cantidad'] += cantidad
    else:
        #se crea el diccionario que contiene la informacion para mostrarla en el carrito
        carrito[producto.id] = {
            'nombre': producto.name,
            'precio': producto.precio,
            'cantidad': cantidad,
            'subtotal': producto.precio * cantidad  #subtotal
        }

    # Actualizar el subtotal después de incrementar la cantidad
    carrito[producto.id]['subtotal'] = carrito[producto.id]['precio'] * carrito[producto.id]['cantidad']

    request.session['carrito'] = carrito
    request.session.modified = True  # Marcar la sesión como modificada

    return redirect('carrito')  





def ver_carrito(request):
    # Obtener el carrito desde la sesión
    carrito = request.session.get('carrito', {})

    # Calcular el total sumando los subtotales
    total = sum(producto['subtotal'] for producto in carrito.values())
    
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})







def vaciar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    return redirect('carrito')  


def base_view(request):
    return render(request, 'base.html')

def menuini(request):
    usuario = None  # Aquí puedes dejar esto vacío o colocar una condición para verificar si el usuario está logueado.
    
    if 'usuario_id' in request.session:
        usuario_id = request.session['usuario_id']
        usuario = Usuario.objects.get(id=usuario_id)

    return render(request, 'menuini.html', {'usuario': usuario})


def accesorios(request):
    return render(request, 'accesorios.html')



def inisesion(request):
    if request.method =='POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if not correo or not password:
            messages.error(request,"favor de completar todos los campos")
            return render(request, 'inisesion.html')
        
        try:
            usuario = Usuario.objects.get(correo=correo) 
            if usuario.check_password(password):  
                request.session['usuario_id'] = usuario.id  
                return redirect('menuini')  
            else:
                messages.error(request, "Correo o contraseña incorrectos.")  
        except Usuario.DoesNotExist:
            messages.error(request, "Correo o contraseña incorrectos.")  

        return render(request, 'inisesion.html')

    return render(request, 'inisesion.html')



def registro(request):
    return render(request, 'registro.html')

def lightper(request):
    return render(request, 'lightper.html')

def ligpix(request):
    return render(request, 'ligpix.html')

def ligrgb(request):
    return render(request, 'ligrgb.html')

def polenvio(request):
    return render(request, 'polenvio.html')

def polgar(request):
    return render(request, 'polgar.html')

def polpri(request):
    return render(request, 'polpri.html')

def prefre(request):
    return render(request, 'prefre.html')







