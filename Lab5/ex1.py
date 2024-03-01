import sys

# Arithmetic operations

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

operands = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
} # Operands

class Stack: # Create stack data structure
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

arg = sys.argv[1] # Receive command prompt argument

if __name__ == '__main__':
    stack = Stack()
    for i in arg:
        if i.isdigit() or i in operands:
            stack.push(i)
        elif i == ')':
            b = stack.pop()
            a = stack.pop()
            op = stack.pop()
            stack.push(operands[op](int(a), int(b)))
    print(stack.pop())
