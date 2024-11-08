from django.contrib import messages  
from django.shortcuts import render, redirect
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
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['productos'])  # Esto imprimirá los productos en la consola
        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'
    context_object_name = 'producto'

def base_view(request):
    return render(request, 'base.html')

def menuini(request):
    # Eliminar la verificación de si el usuario está logueado
    usuario = None  # Aquí puedes dejar esto vacío o colocar una condición para verificar si el usuario está logueado.
    
    if 'usuario_id' in request.session:
        usuario_id = request.session['usuario_id']
        usuario = Usuario.objects.get(id=usuario_id)

    # Pasar el nombre de usuario al template solo si está logueado
    return render(request, 'menuini.html', {'usuario': usuario})


def accesorios(request):
    return render(request, 'accesorios.html')

def carrito(request):
    return render(request, 'carrito.html')

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







