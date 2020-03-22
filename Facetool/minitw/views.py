# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from openpyxl import load_workbook

# Create your views here.
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return redirect('productos')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data ['usuario']
				pas = formulario.cleaned_data ['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return redirect('productos')
				else:
					mensaje = "usuario o clave incorrecta vuelve a intentarlo"
		formulario = Login_form()
		ctx = {'form':formulario, 'mensaje':mensaje}
		return render(request, 'login.html', ctx)


def registrar_persona(request):
	if request.method == "POST":
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
			#Persona = form.save(commit=False)
			#Persona.save()
			return redirect('inicio')
	else:
		form = PersonaForm()
	return render(request, 'registrar.html', locals())



def lista_Producto(request):
	lista = Producto.objects.filter()
	if request.method == "POST":
		form = CantidadForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('inicio')
	else:
		form = CantidadForm()
	return render(request, 'lista_Productos.html', locals())



def Editar_Carrito(request, pk):
	a = get_object_or_404(Carrito, pk=pk)
	if request.method == "POST":
		form = campeonForm(request.POST, request.FILES, instance=a)
		if form.is_valid():
			a = form.save(commit=False)
			a.save()
			return redirect('lista_campeon')
	else:
		f = campeonForm(instance=a)
	return render(request, 'campeon/nuevo_campeon.html', {'form': f})