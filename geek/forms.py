from typing import Any
from django import forms
from .models import Usuario, Producto

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'password','telefono']

    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError("nombre de usuario ya existente!!")
        return nombre_usuario
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Correo ya existe!!")
        return correo
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono) != 9 or not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe tener 9 dígitos numéricos.')
        return telefono
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')

        # me valida que no haya espacios en blanco
        if password and ' ' in password:
            raise forms.ValidationError('La contraseña no puede contener espacios en blanco.')

        # validar que tenga una letra y numero
        if password and (not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password)):
            raise forms.ValidationError('La contraseña debe contener al menos una letra y un número.')

        return cleaned_data

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