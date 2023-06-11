class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def obtener_elementos(self):
        elementos = []
        actual = self.primero
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
    
    def primer_nodo(self):
        return self.primero
