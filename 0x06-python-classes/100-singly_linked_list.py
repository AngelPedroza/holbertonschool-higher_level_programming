#!/usr/bin/python3
class Node:
    """ The clase for simulate a node like a structure in C """

    def __init__(self, data, next_node=None):
        """Init a node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Make a set of data value"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Return the next node of the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Make set the next node of the current node"""
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The class for use each node"""

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        f_str = ""
        while current:
            f_str += str(current.data) + '\n'
            current = current.next_node
        f_str = f_str[:-1]
        return f_str

    def sorted_insert(self, value):

        if self.head is None:
            self.head = Node(value)
        elif self.head.data > value:
            self.head = Node(value, self.head)
        else:
            current = self.head
            while current is not None:
                if current.next_node is None:
                    current.next_node = Node(value)
                    return
                if current.next_node.data > value:
                    current.next_node = Node(value, current.next_node)
                    return
                current = current.next_node
