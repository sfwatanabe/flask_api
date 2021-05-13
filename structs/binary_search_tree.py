"""
Simple example of a binary search tree for flask blog api project.
This version is assuming all keys are unique and will not place a duplicate
key in bst.
"""

class Node:
    """
    Simple Node data structure for the binary search tree class. Holds data and
    references to left and right children.
    """
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data, node):
        """
        Local helper function to recursively place nodes into the binary tree.
        Assumes no duplicates will be stored in the binary search tree and will
        return if an equal value is encountered.

        :param value: Key we want to place into the binary search tree.
        :param node: Node we are currently investigating for placement.
        """
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return

    def insert(self, data):
        """
        Inserts the given value into the binary tree.

        :param data: Key value to insert into the binary search tree.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _search_recursive(self, blog_post_id, node):

        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False

        return self._search_recursive(blog_post_id, self.root)
