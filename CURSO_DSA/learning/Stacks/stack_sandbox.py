from Node import Node
import logging

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0  # Inicializa el tamaño
        self.limit = limit  # Establece el límite

    def push(self, value):
        if not self.has_space():
            logging.warning("La pila esta llena ¡No queda espacio!")  # Mensaje corregido
            return  # Salir si no hay espacio

        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
        self.size += 1  # Incrementar el tamaño

    def pop(self):
        if self.is_empty():
            logging.warning("La pila esta totalmente vacia!")  # Mensaje corregido
            return None  # Cambiar a None en lugar de lanzar una excepción

        item_to_remove = self.top_item
        self.top_item = item_to_remove.next
        self.size -= 1  # Reducir el tamaño al hacer pop
        return item_to_remove.get_value()

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            logging.warning("La pila esta totalmente vacia!")  # Mensaje corregido
            return None  # Devolver None si está vacía

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

