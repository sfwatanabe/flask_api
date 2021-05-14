class Node:
    """
    Basic data node for the stack class data members.
    """
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Stack data structure implementation for flask api project.
    """
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        removed = self.top
        self.top = self.top.next_node
        return removed
