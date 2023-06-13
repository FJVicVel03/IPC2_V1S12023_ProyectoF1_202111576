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
        self.incremental_boletos = 1
        self.lista_compras = []

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
        lista_peliculas = ListaDoblementeEnlazadaCircular()
        lista_salas = []

        # Cargar datos del XML en la lista de películas
        tree_peliculas = ET.parse("peliculas.xml")
        root_peliculas = tree_peliculas.getroot()

        for categoria in root_peliculas.findall('categoria'):
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

        # Cargar datos del XML en la lista de salas
        tree_salas = ET.parse("cines.xml")
        root_salas = tree_salas.getroot()

        for cine in root_salas.findall('cine'):
            for sala_xml in cine.find('salas').findall('sala'):
                numero_sala = sala_xml.find('numero').text
                cantidad_asientos = int(sala_xml.find('asientos').text)
                lista_salas.append((numero_sala, cantidad_asientos))

        # Mostrar las categorías disponibles
        categorias = lista_peliculas.obtener_categorias()
        print("Categorías disponibles:")
        for categoria in categorias:
            print("-", categoria)

        categoria_elegida = input("Seleccione una categoría: ")

        # Obtener y mostrar las películas de la categoría elegida
        peliculas = lista_peliculas.obtener_peliculas(categoria_elegida)
        print("Películas en la categoría", categoria_elegida + ":")
        for i, pelicula in enumerate(peliculas, start=1):
            print("Detalles de Película", i)
            print("Título: ", titulo)
            print("Año: ", anio)
            print("Hora: ", hora)
            print("Fecha: ", fecha)
            print("-----------------")

        pelicula_elegida = int(input("Seleccione una película: ")) - 1
        pelicula_seleccionada = peliculas[pelicula_elegida]

        fecha_funcion = input("Ingrese la fecha de la función (dd/mm/yyyy): ")
        hora_funcion = input("Ingrese la hora de la función (HH:MM): ")
        num_boletos = int(input("Ingrese el número de boletos: "))

        # Obtener la lista de salas disponibles para la película seleccionada
        salas_disponibles = []
        for sala, asientos in lista_salas:
            if asientos >= num_boletos:
                salas_disponibles.append(sala)

        if len(salas_disponibles) == 0:
            print("Lo sentimos, no hay salas disponibles con suficientes asientos.")
            return

        print("Salas disponibles:")
        for i, sala in enumerate(salas_disponibles, start=1):
            print(i, "-", sala)

        sala_elegida = int(input("Seleccione una sala: ")) - 1
        sala_seleccionada = salas_disponibles[sala_elegida]

        asientos_ocupados = []
        for _ in range(num_boletos):
            asiento = input("Ingrese el número de asiento: ")

            if asiento in asientos_ocupados:
                print("El asiento", asiento, "ya está ocupado. Por favor, elija otro.")
                continue

            asientos_ocupados.append(asiento)

        monto_total = num_boletos * 42  # Precio fijo de boletos en efectivo

        print("Monto total a pagar: Q", monto_total)

        opcion_facturacion = input("Ingrese una opción de facturación (nombre, nit, dirección / cf): ")

        if opcion_facturacion.lower() == "cf":
            nombre_facturacion = "Consumidor Final"  # Valor por defecto para facturación cf
            nit_facturacion = ""
            direccion_facturacion = ""
            print("Facturación a Consumidor Final.")

        else:
            nombre_facturacion = input("Ingrese el nombre de facturación: ")
            nit_facturacion = input("Ingrese el NIT de facturación: ")
            direccion_facturacion = input("Ingrese la dirección de facturación: ")

            print("Facturación a nombre de:", nombre_facturacion)
            print("NIT:", nit_facturacion)
            print("Dirección:", direccion_facturacion)

        # Generar el número de boleto
        numero_boleto = "#USACIPC2_" + "202111576" + "_" + str(self.incremental_boletos)
        self.incremental_boletos += 1

        # Guardar la información de la compra y el usuario
        compra = {
            "numero_boleto": numero_boleto,
            "pelicula": pelicula_seleccionada,
            "fecha_funcion": fecha_funcion,
            "hora_funcion": hora_funcion,
            "sala": sala_seleccionada,
            "asientos": asientos_ocupados,
            "monto_total": monto_total,
            "nombre_facturacion": nombre_facturacion,
            "nit_facturacion": nit_facturacion,
            "direccion_facturacion": direccion_facturacion
        }

        self.lista_compras.append(compra)

        print("Compra realizada exitosamente.")
        print("Número de boleto:", numero_boleto)

    
    def historial_boletos_comprados(self):
        print("Historial de boletos comprados:")
        if not self.lista_compras:
            print("No se han realizado compras.")
        else:
            for compra in self.lista_compras:
                print(f"Fecha de compra: {compra['fecha_funcion']}")
                print(f"Nombre: {compra['nombre_facturacion']}")
                print(f"Sala(s): {compra['sala']}")
                print(f"Monto total: {compra['monto_total']}")
                print("------------------------------")