#!/usr/bin/python3
import sys
import py_stack


#DoublyLinkedList = __import__('py_stack').DoublyLinkedList
stack = py_stack.DoublyLinkedList()

#is_stack = True
line_number = 0

functions = {'push':stack.push, 'pall': stack.pall, 'pint': stack.pint,
             'pop':stack.pop, 'swap':stack.swap, 'add':stack.add, 'nop': stack.nop,
             'sub':stack.sub, 'div':stack.div, 'mul':stack.mul, 'mod':stack.mod,
             'pchar':stack.pchar, 'pstr':stack.pstr, 'rotl':stack.rotl,
             'rotr':stack.rotr, 'stack':stack.stack, 'queue':stack.queue}
if len(sys.argv) != 2:
    print("Usage: ./monty.py <filename>")
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            command = line.strip().split()
            line_number += 1
            if command[0] is not None and command[0][0] == '#':
                continue
            if command[0] in functions:
                functions[command[0]](command[1] if len(command) > 1 else None, line_number)
            else:
                print("L{}: unknown instruction {}".format(line_number, command[0]))
except (FileNotFoundError or PermissionError or FileExistsError):
    print("Error: Can't open file {}".format(sys.argv[1]))


