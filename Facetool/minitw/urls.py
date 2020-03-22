from django.conf.urls import url
from.views import * 

urlpatterns = [
		
		#vista principal 
		url(r'^$', login_view, name='inicio'),
		url(r'^registrar$', registrar_persona, name='registro'),
		url(r'^productos$', lista_Producto, name='productos'),


]