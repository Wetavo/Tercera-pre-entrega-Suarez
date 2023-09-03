
from django.contrib import admin
from django.urls import path, include
from Appentrega.views import catedra, lista_catedra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App-entrega/', include("Appentrega.urls")),
    
]
