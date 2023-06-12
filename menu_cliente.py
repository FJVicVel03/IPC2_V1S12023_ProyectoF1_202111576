from pelicula import ListaDoblementeEnlazadaCircular
from pelicula import Pelicula
from favoritas import ListaEnlazada
import copy

import xml.etree.ElementTree as ET

class MenuCliente:
    def __init__(self, lista_peliculas, correo):
        self.lista_peliculas = lista_peliculas
        self.lista_favoritas = ListaEnlazada()
        self.correo = correo

    def mostrar(self):
        while True:
            print("Seleccione una opción:")
            print("1 - Ver Listado de Películas")
            print("2 - Listado de Películas Favoritas")
            print("3 - Comprar Boletos")
            print("4 - Historial de Boletos Comprados")
            print("5 - Salir")

            opc = input("Ingrese el número de opción: ")

            if opc == "1":
                self.ver_listado_peliculas()
            
            elif opc == "2":
                self.listado_peliculas_favoritas()
            
            elif opc == "3":
                self.comprar_boletos()
            
            elif opc == "4":
                self.historial_boletos_comprados()
            
            elif opc == "5":
                print("Saliendo del menú de cliente...")
                break
            
            else:
                print("Opción inválida. Intente nuevamente.")
    
    def ver_listado_peliculas(self):
        lista_peliculas = ListaDoblementeEnlazadaCircular()
        
        # Cargar datos del XML en la lista
        tree = ET.parse("peliculas.xml")
        root = tree.getroot()

        for categoria in root.findall('categoria'):
            nombre_categoria = categoria.find('nombre').text
            lista_peliculas.agregar_categoria(nombre_categoria)

            for pelicula_xml in categoria.find('peliculas').findall('pelicula'):
                titulo = pelicula_xml.find('titulo').text
                director = pelicula_xml.find('director').text
                anio = pelicula_xml.find('anio').text
                fecha = pelicula_xml.find('fecha').text
                hora = pelicula_xml.find('hora').text

                peli = Pelicula(titulo, director, anio, fecha, hora)  # Crear instancia de Pelicula
                
                lista_peliculas.agregar_pelicula(nombre_categoria, titulo, director, anio, fecha, hora)
                
                # Obtener y mostrar las categorías
                categorias = lista_peliculas.obtener_categorias()
                print("Categorías disponibles:")
                for categoria in categorias:
                    print("-", categoria)

                categoria_elegida = input("Seleccione una categoría: ")

                # Obtener y mostrar las películas de la categoría elegida
                peliculas = lista_peliculas.obtener_peliculas(categoria_elegida)
                print("Películas en la categoría", categoria_elegida + ":")
                for i, pelicula in enumerate(peliculas, start=1):
                    print("Detalles de Películas:", i)
                    print("Titulo: ", titulo)
                    print("Año: ", anio)
                    print("Hora: ", hora)
                    print("Fecha: ", fecha)
                    print("-----------------")
                    
                    # Solicitar al usuario si desea marcar la película como favorita
                    respuesta = input("¿Desea marcar esta película como favorita? (s/n): ")
                    if respuesta.lower() == "s":
                        pelicula_favorita = copy.deepcopy(pelicula)
                        self.agregar_pelicula_favorita(pelicula_favorita)  # Agrega la película a la lista de favoritos
  
    def agregar_pelicula_favorita(self, pelicula):
        self.correo_usuario = self.correo  # Asigna el correo del usuario a pelicula.correo_usuario
        self.lista_favoritas.agregar(pelicula)  # Agrega la película a la lista de favoritos del usuario
        print("Película agregada a tus favoritos.")

     

    def listado_peliculas_favoritas(self):
        if self.lista_favoritas.esta_vacia():
            print("No tienes películas favoritas.")
            return

        print("Películas favoritas:")
        pelicula_actual = self.lista_favoritas.primer_nodo()
        while pelicula_actual is not None:
            pelicula = pelicula_actual.dato

            print(pelicula)

            pelicula_actual = pelicula_actual.siguiente

    
    def comprar_boletos(self):
        # Lógica para comprar boletos
        print("Comprando boletos...")
        # Aquí puedes llamar a los métodos correspondientes para comprar boletos
    
    def historial_boletos_comprados(self):
        # Lógica para mostrar el historial de boletos comprados
        print("Mostrando historial de boletos comprados...")
        # Aquí puedes llamar a los métodos correspondientes para mostrar el historial de boletos comprados
