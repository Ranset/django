from django.shortcuts import render

from .models import Directores, Peliculas

def index (request):
    directores = Directores.objects.all()

    return render(request, 'index.html', context={
        'directores': directores,
    })

# Capturando la variable ids pasada en la url
# El nombre de la variable debe coincidir con introducido en urls.py
def director (request, ids):
    dtor = Directores.objects.filter(id = ids)
    foto =''
    nombre = ''
    apellido = ''
    nacimiento= ''
    muerte = ''
    pais = ''
    biografia = ''
    peliculas = Peliculas.objects.filter(director = ids)

    for director in dtor:
        foto = director.foto
        nombre = director.nombre
        apellido = director.apellido
        nacimiento = director.nacimiento
        if director.fallecimiento:
            muerte = f' † {director.fallecimiento}'
        else:
            muerte = ''
        pais = director.pais
        biografia = director.biografia
        

    return render(request, 'Details.html',context={
        'nombre': nombre,
        'apellido': apellido,
        'fechas': f'{nacimiento} {muerte}',
        'foto': foto,
        'pais': pais,
        'bio': biografia,
        'peliculas' : peliculas
    })

def pelicula (request, ids):
    peliculas = Peliculas.objects.filter(id = ids)

    # Haciendo un switch para colocar el nombre correcto del género
    genero = ''

    for peli in peliculas:
        if peli.genero == 'c':
            genero = 'Comedia'
        elif peli.genero == 'f':
            genero = 'Ciencia Ficción'
        elif peli.genero == 'd':
            genero = 'Drama'
        elif peli.genero == 't':
            genero = 'Terror'

    return render(request, 'pelis.html',context={
        'peliculas': peliculas,
        'genero': genero
    })
