from django.contrib.auth import authenticate, login
from django.contrib import messages  


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Usuario, Producto
from .forms import UsuarioForm, ProductoForm
from django.urls import reverse_lazy

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'registro.html'
    success_url = reverse_lazy('menuini')  

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


def base_view(request):
    return render(request, 'base.html')

def menuini(request):
    if 'usuario_id' not in request.session:
        return redirect('inisesion')  # Redirigir a inicio de sesión si no está autenticado

    usuario_id = request.session['usuario_id']
    usuario = Usuario.objects.get(id=usuario_id)

    # Aquí puedes renderizar la plantilla o hacer lo que necesites
    return render(request, 'menuini.html', {'usuario': usuario})


def accesorios(request):
    return render(request, 'accesorios.html')

def carrito(request):
    return render(request, 'carrito.html')



def inisesion(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(correo=email)  # Buscar el usuario por correo
            if usuario.check_password(password):  # Verificar la contraseña
                # Almacenar el ID del usuario en la sesión
                request.session['usuario_id'] = usuario.id  
                return redirect('menuini')  # Redirigir al menú principal
        except Usuario.DoesNotExist:
            pass  # El usuario no existe

        # Autenticación fallida
        messages.error(request, "Correo o contraseña incorrectos")  # Mensaje de error
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







