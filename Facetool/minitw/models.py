# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.


class Persona(models.Model):
	nombre = models.CharField(null=True, max_length=25)
	apellido = models.CharField(null=True, max_length=25)
	cedula = models.IntegerField(primary_key=True)
	direccion = models.CharField(null=True, max_length=25)
	fecha_nacimiento = models.DateField(null=True, max_length=255)
	descripcion = models.TextField(null=True)

	def __unicode__ (self):
		return self.nombre

	
class Producto(models.Model):
	custom_id = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=255)
	precio = models.FloatField()
	imagen = models.ImageField(upload_to='Facetool/media/')

	def __unicode__(self):
		return self.nombre


class Carrito(models.Model):
	Cantidad = models.FloatField(null=True, blank=True)
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return self.Cantidad


