from Node import Node
import logging
class Stack:
    def __init__(self):
        self.top_item = None
    def push(self, value):
        item = Node(value)  # Crear un nuevo nodo
        item.set_next_node(self.top_item)  # Establecer el siguiente nodo
        self.top_item = item  # Actualizar el top_item
    def pop(self):
        if self.top_item is None:
            logging.warning("No se puede hacer pop en una pila vacía.")
            raise AttributeError("No se puede hacer pop en una pila vacía.")
        item_to_remove = self.top_item  # Guardar el item a eliminar
        self.top_item = item_to_remove.next  # Actualizar el top_item
        return item_to_remove.get_value()
    
    def peek(self):
        if self.top_item is not None:
            return self.top_item.get_value()
        else:
            logging.warning("La pila está vacía. No se puede hacer peek.")
            raise AttributeError("No se puede hacer peek en una pila vacía.")