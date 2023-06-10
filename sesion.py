import xml.etree.ElementTree as ET

class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.siguiente = None

class InicioSesion:
    def __init__(self):
        self.tree = ET.parse("usuarios.xml")
        self.root = self.tree.getroot()

    def obtener_usuarios(self):
        usuarios = None
        ultimo_usuario = None

        # Recorrer los elementos 'usuario'
        for usuario in self.root.findall('usuario'):
            rol = usuario.find('rol').text
            nombre = usuario.find('nombre').text
            apellido = usuario.find('apellido').text
            telefono = usuario.find('telefono').text
            correo = usuario.find('correo').text
            contrasena = usuario.find('contrasena').text

            nuevo_usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)

            if usuarios is None:
                usuarios = nuevo_usuario
                ultimo_usuario = nuevo_usuario
            else:
                ultimo_usuario.siguiente = nuevo_usuario
                ultimo_usuario = nuevo_usuario

        return usuarios

    def buscar_usuario(self, correo, contrasena):
        usuarios = self.obtener_usuarios()

        # Recorrer la lista enlazada de usuarios
        usuario_actual = usuarios
        while usuario_actual is not None:
            # Comprobar si el correo y la contraseña coinciden
            if usuario_actual.correo == correo and usuario_actual.contrasena == contrasena:
                return usuario_actual.rol

            usuario_actual = usuario_actual.siguiente

        return None

    def mostrar_usuarios(self):
        usuarios = self.obtener_usuarios()

        # Recorrer la lista enlazada de usuarios
        usuario_actual = usuarios
        while usuario_actual is not None:
            # Imprimir información del usuario
            print("Rol:", usuario_actual.rol)
            print("Nombre:", usuario_actual.nombre)
            print("Apellido:", usuario_actual.apellido)
            print("Teléfono:", usuario_actual.telefono)
            print("Correo:", usuario_actual.correo)
            print("Contraseña:", usuario_actual.contrasena)
            print()

            usuario_actual = usuario_actual.siguiente

# Crear una instancia de la clase InicioSesion
sesion = InicioSesion()

# Llamar al método para mostrar los usuarios
sesion.mostrar_usuarios()
