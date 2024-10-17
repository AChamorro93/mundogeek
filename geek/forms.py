from django import forms
from .models import Usuario, Producto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'password', 'telefono']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre_usuario = cleaned_data.get('nombre_usuario')
        correo = cleaned_data.get('correo')

        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            self.add_error('nombre_usuario', '¡Nombre de Usuario Ya en Uso!')

        if Usuario.objects.filter(correo=correo).exists():
            self.add_error('correo', '¡Correo Ya en Uso!')


        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len (password) < 8:
            raise forms.ValidationError('!La contraseña debe tener minimo 8 caracteres!')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('!La contraseña debe tener al menos 1 numero!')
        return password

class ProductoForm(forms.ModelForm):
    TECNOLOGIA_CHOICES = {
        ('RGB','RGB'),
        ('NEOPIXEL','NEOPIXEL'),
    }

    COLOR_CHOICES = {
        ('Negro','Negro'),
        ('Gris','Gris'),
        ('Plateado','Plateado'),
        ('Dorado','Dorado'),
        ('Rojo','Rojo'),
        ('Azul','Azul'),
        ('Blanco','Blanco'),
        (None,'None'), 
    }
    tecnologia = forms.ChoiceField(choices= TECNOLOGIA_CHOICES, widget=forms.RadioSelect)
    color = forms.ChoiceField(choices= COLOR_CHOICES, widget=forms.RadioSelect)


    class Meta:
        model = Producto
        fields = '__all__'