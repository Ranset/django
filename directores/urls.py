from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # Pasando una variable por url   /<Tipo:nombre>/
    # El nombre de la variable debe coincidir con nombre del parámetro en views.py
    path('director/<int:ids>/', views.director, name='director'),
    path('pelicula/<int:ids>/', views.pelicula, name='pelicula'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
