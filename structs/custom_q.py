class Node:
    """
    Simple node class for holding member data of the queue class.
    """
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    """
    Queue structure for our blog api project.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Adds nodes to tail of the list.
        :param data: Data member to be added to the queue.
        """
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        """
        Pulls from the front of the queue.
        :return: Data member from the head of the queue.
        """
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None
        return removed
