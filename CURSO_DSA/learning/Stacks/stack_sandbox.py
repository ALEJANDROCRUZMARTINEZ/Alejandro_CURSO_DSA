from Node import Node
import logging
class Stack:
    def __init__(self):
        self.top_item = None
    def push(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.top_item)  # Establece el siguiente nodo
        self.top_item = new_node  # Actualiza el nodo superior
    def peek(self):
        if self.top_item is not None:
            return self.top_item.get_value()
        else:
            logging.warning("La pila está vacía. No se puede hacer peek.")
            raise AttributeError("No se puede hacer peek en una pila vacía.")