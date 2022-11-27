from datetime import date
from django.db import models

class Directores (models.Model):
    foto = models.URLField(null= True, blank= True, help_text='Coloque la dirección URL de la foto')
    nombre = models.CharField(max_length = 64, help_text = 'Coloca el nombre del director')
    apellido = models.CharField(max_length = 64, null = True)
    nacimiento = models.DateField(default=date.today, auto_now=False, auto_now_add=False)
    fallecimiento = models.DateField(help_text = 'Si sigue vivo dejar en blanco', null = True, blank = True)
    pais = models.CharField(max_length= 64, null= True)
    biografia = models.TextField(null= True)


    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'


class Peliculas (models.Model):
    poster = models.URLField(null= True, blank= True, help_text='Coloque la dirección URL de la foto')
    titulo = models.CharField(max_length= 64)
    pais = models.CharField(max_length= 64)
    duracion = models.PositiveIntegerField(help_text='Poner la duración en minutos')

    tipo = (
        ('c', 'Comedia'),
        ('f', 'Ciencia Ficción'),
        ('d','drama'),
        ('t','Terror')
    )
    
    genero = models.CharField(max_length= 1, choices = tipo, blank= True)

    director = models.ForeignKey('Directores', on_delete = models.SET_NULL, null = True)

    sinopsis = models.TextField()


    def __str__(self):
        return self.titulo