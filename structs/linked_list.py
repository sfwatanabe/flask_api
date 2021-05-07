"""
Simple linked list data structure for flask api project structure.
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)

        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node


ll = LinkedList()
# node4 = Node("4", None)
ll.insert_beginning(0)
ll.insert_at_end(7)
ll.insert_beginning(9)
ll.insert_beginning(1)
ll.insert_at_end(7)
ll.insert_beginning(1)
ll.insert_beginning(13)
ll.insert_at_end(4)
ll.insert_beginning(6)
ll.insert_beginning(1)
ll.insert_at_end(7)
ll.insert_beginning(9)
ll.insert_beginning(1)

ll.print_ll()
