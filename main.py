from sesion import InicioSesion
from pelicula import ListaDoblementeEnlazadaCircular
import xml.etree.ElementTree as ET

class Main:
    
    @staticmethod
    def ejecutar():
        lista_peliculas = ListaDoblementeEnlazadaCircular()

        # Cargar datos del XML en la lista
        tree = ET.parse("peliculas.xml")
        root = tree.getroot()

        for categoria in root.findall('categoria'):
            nombre_categoria = categoria.find('nombre').text
            lista_peliculas.agregar_categoria(nombre_categoria)

            for pelicula in categoria.find('peliculas').findall('pelicula'):
                titulo = pelicula.find('titulo').text
                director = pelicula.find('director').text
                anio = pelicula.find('anio').text
                fecha = pelicula.find('fecha').text
                hora = pelicula.find('hora').text

                lista_peliculas.agregar_pelicula(nombre_categoria, titulo, director, anio, fecha, hora)

        while True:
            print("Bienvenido, seleccione una opción:")
            print("1 - Iniciar Sesión")
            print("2 - Registrar Usuario")
            print("3 - Ver listado de películas")
            print("- - - - - - - - - - - - - - - - - -")

            opc = input("Seleccione una opción: ")

            if opc == "1":
                print("Ha seleccionado Iniciar Sesión")
                sesion = InicioSesion()

                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")

                rol = sesion.buscar_usuario(correo, contrasena)

                if rol is not None:
                    print("Tu rol es:", rol)
                    if rol == "administrador":
                        #aquí va el menú de administrador
                        pass
                    elif rol == "cliente":
                        #aquí va el menú de cliente
                        pass
                else:
                    print("Correo o contraseña incorrectos.")
            
            elif opc == "2":
                print("Ha seleccionado Registrar Usuario")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese apellido: ")
                telefono = input("Ingrese número de teléfono: ")
                correo = input("Ingrese el correo: ")
                password = input("Ingrese la contraseña: ")
                rol = "cliente"

                # Crear el nuevo elemento de usuario
                nuevo_usuario = ET.Element("usuario")

                # Crear los elementos hijos y asignarles los valores
                ET.SubElement(nuevo_usuario, "rol").text = rol
                ET.SubElement(nuevo_usuario, "nombre").text = nombre
                ET.SubElement(nuevo_usuario, "apellido").text = apellido
                ET.SubElement(nuevo_usuario, "telefono").text = telefono
                ET.SubElement(nuevo_usuario, "correo").text = correo
                ET.SubElement(nuevo_usuario, "contrasena").text = password

                # Agregar el nuevo usuario al elemento raíz
                sesion.root.append(nuevo_usuario)

                # Guardar los cambios en el archivo
                sesion.tree.write("usuarios.xml")

                print("Usuario registrado exitosamente.")
                continue  # Continuar con el siguiente ciclo del bucle
            
            elif opc == "3":
                print("Ha seleccionado Ver listado de películas")

                # Obtener y mostrar las categorías
                categorias = lista_peliculas.obtener_categorias()
                print("Categorías disponibles:")
                for categoria in categorias:
                    print("-", categoria)

                categoria_elegida = input("Seleccione una categoría: ")

                # Obtener y mostrar las películas de la categoría elegida
                peliculas = lista_peliculas.obtener_peliculas(categoria_elegida)
                print("Películas en la categoría", categoria_elegida + ":")
                for pelicula in peliculas:
                    print("-", pelicula)

            else:
                print("Opción inválida. Saliendo del programa.")
                break  # Salir del bucle y finalizar el programa

# Ejecutar el programa
Main.ejecutar()
