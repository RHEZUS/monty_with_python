#!/usr/bin/python3
import sys
import py_stack


#DoublyLinkedList = __import__('py_stack').DoublyLinkedList
stack = py_stack.DoublyLinkedList()

#is_stack = True
line_number = 0

functions = {'push':stack.push, 'pall': stack.pall, 'pint': stack.pint, 'pop':stack.pop}
if len(sys.argv) != 2:
    print("Usage: ./monty.py <filename>")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        command = line.strip().split()
        line_number += 1
        try:
            functions[command[0]](command[1] if len(command) > 1 else None, line_number)
        except:
            print("L{}: unknown instruction {}".format(line_number, command[0]))


