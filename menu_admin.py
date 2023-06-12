import xml.etree.ElementTree as ET

class MenuAdmin:
    def mostrar(self):
        while True:
            print("=== Menú de Administrador ===")
            print("1. Gestionar Usuarios")
            print("2. Gestionar Categorías y Películas")
            print("3. Gestionar Salas")
            print("4. Gestionar Boletos Comprados")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_usuarios()
            elif opcion == "2":
                self.gestionar_categorias_peliculas()
            elif opcion == "3":
                self.gestionar_salas()
            elif opcion == "4":
                self.gestionar_boletos_comprados()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                
#Esto es lo de la gestión de usuarios
    def gestionar_usuarios(self):
        while True:
            print("=== Gestión de Usuarios ===")
            print("1. Ver Usuarios")
            print("2. Agregar Usuario")
            print("3. Eliminar Usuario")
            print("0. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_usuarios()
            elif opcion == "2":
                self.agregar_usuario()
            elif opcion == "3":
                self.eliminar_usuario()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def ver_usuarios(self):
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()

        for usuario in root.findall("usuario"):
            rol = usuario.find("rol").text
            nombre = usuario.find("nombre").text
            apellido = usuario.find("apellido").text
            telefono = usuario.find("telefono").text
            correo = usuario.find("correo").text
            contrasena = usuario.find("contrasena").text

            print("Rol:", rol)
            print("Nombre:", nombre)
            print("Apellido:", apellido)
            print("Teléfono:", telefono)
            print("Correo:", correo)
            print("Contraseña:", contrasena)
            print("---------------------")

    def agregar_usuario(self):
        print("=== Agregar Usuario ===")
        rol = input("Rol: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        tree = ET.parse("usuarios.xml")
        root = tree.getroot()

        usuario = ET.SubElement(root, "usuario")
        ET.SubElement(usuario, "rol").text = rol
        ET.SubElement(usuario, "nombre").text = nombre
        ET.SubElement(usuario, "apellido").text = apellido
        ET.SubElement(usuario, "telefono").text = telefono
        ET.SubElement(usuario, "correo").text = correo
        ET.SubElement(usuario, "contrasena").text = contrasena

        tree.write("usuarios.xml")
        print("Usuario agregado exitosamente.")

    def eliminar_usuario(self):
        print("=== Eliminar Usuario ===")
        correo = input("Correo del usuario a eliminar: ")

        tree = ET.parse("usuarios.xml")
        root = tree.getroot()

        usuario = root.find(f"./usuario[correo='{correo}']")
        if usuario is not None:
            root.remove(usuario)
            tree.write("usuarios.xml")
            print("Usuario eliminado exitosamente.")
        else:
            print("No se encontró ningún usuario con el correo especificado.")

#Esto es lo de las películas... larguísimo xdd
    def gestionar_categorias_peliculas(self):
        tree = ET.parse("peliculas.xml")
        root = tree.getroot()

        while True:
            print("\n--- GESTIÓN DE CATEGORÍAS Y PELÍCULAS ---")
            print("1. Ver categorías")
            print("2. Ver películas de una categoría")
            print("3. Agregar categoría")
            print("4. Agregar película a una categoría")
            print("5. Modificar categoría")
            print("6. Modificar película")
            print("7. Eliminar categoría")
            print("8. Eliminar película")
            print("9. Regresar al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_categorias(root)
            elif opcion == "2":
                self.ver_peliculas_categoria(root)
            elif opcion == "3":
                self.agregar_categoria(root)
                tree.write("peliculas.xml")
            elif opcion == "4":
                self.agregar_pelicula_categoria(root)
                tree.write("peliculas.xml")
            elif opcion == "5":
                self.modificar_categoria(root)
                tree.write("peliculas.xml")
            elif opcion == "6":
                self.modificar_pelicula(root)
                tree.write("peliculas.xml")
            elif opcion == "7":
                self.eliminar_categoria(root)
                tree.write("peliculas.xml")
            elif opcion == "8":
                self.eliminar_pelicula(root)
                tree.write("peliculas.xml")
            elif opcion == "9":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def ver_categorias(self, root):
        print("\n--- CATEGORÍAS ---")
        for categoria in root.findall('categoria'):
            nombre_categoria = categoria.find('nombre').text
            print("- ", nombre_categoria)

    def ver_peliculas_categoria(self, root):
        categoria_elegida = input("Ingrese el nombre de la categoría: ")
        categoria = root.find(".//categoria[nombre='" + categoria_elegida + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        print("\n--- PELÍCULAS DE", categoria_elegida.upper(), "---")
        peliculas = categoria.findall('peliculas/pelicula')
        for pelicula in peliculas:
            titulo = pelicula.find('titulo').text
            director = pelicula.find('director').text
            anio = pelicula.find('anio').text
            fecha = pelicula.find('fecha').text
            hora = pelicula.find('hora').text
            print("Título:", titulo)
            print("Director:", director)
            print("Año:", anio)
            print("Fecha:", fecha)
            print("Hora:", hora)
            print("-------------------")

    def agregar_categoria(self, root):
        nombre_categoria = input("Ingrese el nombre de la categoría: ")

        # Verificar si la categoría ya existe
        categoria_existente = root.find(".//categoria[nombre='" + nombre_categoria + "']")
        if categoria_existente is not None:
            print("La categoría ya existe.")
            return

        # Crear el elemento de la nueva categoría
        nueva_categoria = ET.Element('categoria')
        nombre = ET.SubElement(nueva_categoria, 'nombre')
        nombre.text = nombre_categoria
        peliculas = ET.SubElement(nueva_categoria, 'peliculas')

        # Agregar la nueva categoría al root
        root.append(nueva_categoria)
        print("Categoría agregada correctamente.")

    def agregar_pelicula_categoria(self, root):
        categoria_elegida = input("Ingrese el nombre de la categoría: ")
        categoria = root.find(".//categoria[nombre='" + categoria_elegida + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el director de la película: ")
        anio = input("Ingrese el año de la película: ")
        fecha = input("Ingrese la fecha de la película (YYYY-MM-DD): ")
        hora = input("Ingrese la hora de la película (HH:MM): ")

        # Crear el elemento de la nueva película
        nueva_pelicula = ET.Element('pelicula')
        titulo_element = ET.SubElement(nueva_pelicula, 'titulo')
        titulo_element.text = titulo
        director_element = ET.SubElement(nueva_pelicula, 'director')
        director_element.text = director
        anio_element = ET.SubElement(nueva_pelicula, 'anio')
        anio_element.text = anio
        fecha_element = ET.SubElement(nueva_pelicula, 'fecha')
        fecha_element.text = fecha
        hora_element = ET.SubElement(nueva_pelicula, 'hora')
        hora_element.text = hora

        # Agregar la nueva película a la categoría
        peliculas = categoria.find('peliculas')
        peliculas.append(nueva_pelicula)
        print("Película agregada correctamente.")

    def modificar_categoria(self, root):
        nombre_categoria = input("Ingrese el nombre de la categoría a modificar: ")
        categoria = root.find(".//categoria[nombre='" + nombre_categoria + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
        categoria.find('nombre').text = nuevo_nombre
        print("Categoría modificada correctamente.")

    def modificar_pelicula(self, root):
        categoria_elegida = input("Ingrese el nombre de la categoría: ")
        categoria = root.find(".//categoria[nombre='" + categoria_elegida + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        titulo_pelicula = input("Ingrese el título de la película a modificar: ")
        pelicula = categoria.find(".//pelicula[titulo='" + titulo_pelicula + "']")
        if pelicula is None:
            print("La película no existe.")
            return

        nuevo_titulo = input("Ingrese el nuevo título de la película: ")
        pelicula.find('titulo').text = nuevo_titulo
        nuevo_director = input("Ingrese el nuevo director de la película: ")
        pelicula.find('director').text = nuevo_director
        nuevo_anio = input("Ingrese el nuevo año de la película: ")
        pelicula.find('anio').text = nuevo_anio
        nueva_fecha = input("Ingrese la nueva fecha de la película (YYYY-MM-DD): ")
        pelicula.find('fecha').text = nueva_fecha
        nueva_hora = input("Ingrese la nueva hora de la película (HH:MM): ")
        pelicula.find('hora').text = nueva_hora
        print("Película modificada correctamente.")

    def eliminar_categoria(self, root):
        nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
        categoria = root.find(".//categoria[nombre='" + nombre_categoria + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        root.remove(categoria)
        print("Categoría eliminada correctamente.")

    def eliminar_pelicula(self, root):
        categoria_elegida = input("Ingrese el nombre de la categoría: ")
        categoria = root.find(".//categoria[nombre='" + categoria_elegida + "']")
        if categoria is None:
            print("La categoría no existe.")
            return

        titulo_pelicula = input("Ingrese el título de la película a eliminar: ")
        pelicula = categoria.find(".//pelicula[titulo='" + titulo_pelicula + "']")
        if pelicula is None:
            print("La película no existe.")
            return

        categoria.find('peliculas').remove(pelicula)
        print("Película eliminada correctamente.")

#Esto es lo de la gestión de las salas
    def gestionar_salas(self):
        while True:
            print("=== Gestión de Salas ===")
            print("1. Ver Salas")
            print("2. Agregar Sala")
            print("3. Eliminar Sala")
            print("0. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_salas()
            elif opcion == "2":
                self.agregar_sala()
            elif opcion == "3":
                self.eliminar_sala()
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def ver_salas(self):
        tree = ET.parse("cines.xml")
        root = tree.getroot()

        for cine in root.findall("cine"):
            nombre_cine = cine.find("nombre").text
            print(f"Salas disponibles en {nombre_cine}:")
            salas = cine.find("salas")
            for sala in salas.findall("sala"):
                numero_sala = sala.find("numero").text
                asientos = sala.find("asientos").text
                print(f"Número de sala: {numero_sala}")
                print(f"Asientos disponibles: {asientos}")
                print("-------------------------")

    def agregar_sala(self):
        print("=== Agregar Sala ===")
        numero_sala = input("Ingrese el número de sala: ")
        asientos = input("Ingrese la cantidad de asientos disponibles: ")

        tree = ET.parse("cines.xml")
        root = tree.getroot()

        cine = root.find("cine")
        salas = cine.find("salas")

        nueva_sala = ET.SubElement(salas, "sala")
        nuevo_numero = ET.SubElement(nueva_sala, "numero")
        nuevo_numero.text = numero_sala
        nuevos_asientos = ET.SubElement(nueva_sala, "asientos")
        nuevos_asientos.text = asientos

        tree.write("cines.xml")
        print("Sala agregada exitosamente.")

    def eliminar_sala(self):
        print("=== Eliminar Sala ===")
        numero_sala = input("Ingrese el número de sala a eliminar: ")

        tree = ET.parse("cines.xml")
        root = tree.getroot()

        cine = root.find("cine")
        salas = cine.find("salas")

        for sala in salas.findall("sala"):
            numero = sala.find("numero").text
            if numero == numero_sala:
                salas.remove(sala)
                tree.write("cines.xml")
                print("Sala eliminada exitosamente.")
                return

        print("No se encontró ninguna sala con el número especificado.")


# Programa principal
def main():
    menu_admin = MenuAdmin()
    menu_admin.mostrar()
    menu_admin.gestionar_categorias_peliculas()
    menu_admin.gestionar_salas()

if __name__ == "__main__":
    main()
