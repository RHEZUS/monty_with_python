#!/usr/bin/python3
from typing import Any
import sys


is_stack = True


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, prev_node=None, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def prev_node(self):
        """Get/set the next_node of the Node."""
        return (self.__prev_node)

    @prev_node.setter
    def prev_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__prev_node = value


    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    @property
    def get_head(self):
        return self.__head
    @property
    def get_tail(self):
        return self.__tail
    
    def add_node(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.prev_node = None

        new_node.next_node = self.head

        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node
        
    
    def add_node_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next_node = None
            new_node.prev_node = None
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            new_node.next_node = None
            new_node.prev_node = current.prev_node
            current.next_node = new_node

    def push(self, data, line_number):
        if data == None:
            print("L{}: usage: push integer".format(line_number))
            sys.exit(1)
        try:
            data = int(data)
        except:
            print("L{}: usage: push integer", format(line_number))
            sys.exit(1)

        if is_stack:
            self.add_node(data)
        else:
            self.add_node_end(data)


        #print("push, ".format(data))
    
    def pall(self, command, line_number):
        head = self.head
        if head is None:
            return
        while head is not None:
            print("{}".format(head.data))
            head = head.next_node
        #print(self)
    def pint(self, command, line_number):
        head = self.head
        if head is None:
            return
        print("{}".format(head.data))
    
    def pop(self, command, line_number):
        head = self.head
        self.head = head.next_node
        head = None

    def swap(self, command, line_number):
        current = self.head
        length = 0
        data = 0
        while (current != None):
            length += 1
            current = current.next_node
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        data = self.head.data
        self.head.data = self.head.next_node.data
        self.head.next_node.data = data

    def add(self, command, line_number):
        result = 0
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next_node
            #print(length)
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        #print("Add")
        result = self.head.data + self.head.next_node.data
        self.head.next_node.data = result
        
        head = self.head
        self.head = head.next_node
        head = None
        
    def nop(self, command, line_number):
        pass
    def sub(self, command, line_number):
        result = 0
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next_node
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        #print("Add")
        result = self.head.next_node.data - self.head.data
        self.head.next_node.data = result

        head = self.head
        self.head = head.next_node
        head = None
    def div(self, command, line_number):
        result = 0
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next_node
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        #print("Add")
        result = self.head.next_node.data // self.head.data
        self.head.next_node.data = result

        head = self.head
        self.head = head.next_node
        head = None
    def mul(self, command, line_number):
        result = 0
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next_node
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        #print("Add")
        result = self.head.next_node.data * self.head.data
        self.head.next_node.data = result

        head = self.head
        self.head = head.next_node
        head = None
    def mod(self, command, line_number):
        result = 0
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next_node
        if length < 2:
            print("L{}: can't swap, stack too short".format(line_number))
            sys.exit(1)
        #print("Add")
        result = self.head.next_node.data % self.head.data
        self.head.next_node.data = result

        head = self.head
        self.head = head.next_node
        head = None
    

    def pchar(self, command, line_number):
        head = self.head
        if head is None:
            print("L{}: can't pchar, stack empty".format(line_number))
            sys.exit(1)
        if head.data < 0 or head.data > 127:
            print("L{}: can't pchar, value out of range".format(line_number))
            sys.exit(1)
        print("{}".format(chr(head.data)))

    def pstr(self, command, line_number):
        head = self.head
        if head is None:
            print()
        while head is not None:
            if head.data <= 0 or head.data > 127:
                break
            else:
                print("{}".format(chr(head.data)), end="")
            head = head.next_node
        print()

    def rotl(self, command, line_number):
        if self.head is None or self.head.next_node is None:
            return
        head = self.head.next_node
        head.prev_node = None
        tmp  = self.head
        while tmp.next_node is not None:
            tmp = tmp.next_node
        tmp.next_node = self.head
        self.head.next_node = None
        self.head.prev_node = tmp
        self.head = head
    
    def  rotr(self, command, line_number):
        if self.head is None or self.head.next_node is None:
            return
        copy = self.head
        while copy.next_node is not None:
            copy = copy.next_node
        copy.next_node = self.head
        copy.prev_node.next_node = None
        copy.prev_node = None
        self.head.prev_node = copy
        self.head = copy

    def stack(self, command, line_number):
        global is_stack
        is_stack = True

    def queue(self, command, line_number):
        global is_stack
        is_stack = False

