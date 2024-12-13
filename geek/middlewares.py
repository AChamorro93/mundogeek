# geek/middlewares.py
from django.utils.deprecation import MiddlewareMixin

class CartInitializationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verificar si el carrito ya existe en la sesión, si no, inicializarlo
        if "carrito" not in request.session:
            request.session["carrito"] = {}
            request.session.modified = True  # Asegura que la sesión se marque como modificada


