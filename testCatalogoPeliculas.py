from Domain.Pelicula import Pelicula
from Service.CatalogoPeliculas import CatalogoPeliculas as cp


option = None
while option != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar Pelicula')
        print('3. Eliminar catalogo peliculas')
        print('4. Salir')
        option = int(input('Escriba tu opcion (1-4): '))
        if option == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif option == 2:
            cp.listar_peliculas()
        elif option == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        option = None
else:
    print('Salimos del programa')
    print('Adios!')
