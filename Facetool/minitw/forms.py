from django import forms
from .models import *
from django.contrib.auth.models import User

class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))



class PersonaForm(forms.ModelForm):
	class Meta:
			model = Persona
			fields = ['nombre','apellido','direccion','fecha_nacimiento','descripcion']



class CantidadForm(forms.ModelForm):
	class Meta:
			model = Carrito
			fields = ['Cantidad']

