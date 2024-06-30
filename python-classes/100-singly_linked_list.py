#!/usr/bin/python3
"""
100-singly_linked_list module

This module defines classes Node and SinglyLinkedList to implemen

"""


class Node:
    """
    Node class for a singly linked list.

    Attributes:
        __data (int): Data stored in the node.
        __next_node (Node): Reference to the next node in the linked list.

    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with data and optionally a reference to the n

        Args:
            data (int): Data to be stored in the node.
            next_node (Node, optional): Reference to the next n

        Raises:
            TypeError: If data is not an integer or next_node is not No

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute.

        Returns:
            int: Data stored in the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data attribute.

        Args:
            value (int): New value for data.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node attribute.

        Returns:
            Node or None: Next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node attribute.

        Args:
            value (Node or None): New value for next_node.

        Raises:
            TypeError: If value is neither None nor a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class to manage a singly linked list.

    Attributes:
        head (Node): Reference to the head node of the linked list.

    """

    def __init__(self):
        """
        Initializes an empty singly linked list with head set to None.

        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: String representation of the linked list, each node
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct solist (ascending order).

        Args:
            value (int): Value to be inserted into the linked list.

        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    # Example of inserting sorted values
    values_to_insert = [2, 5, 3, 10, 1, -4, -3, 4, 5, 12, 3]
    for value in values_to_insert:
        singly_linked_list.sorted_insert(value)
    # Printing the linked list
    print(singly_linked_list)
