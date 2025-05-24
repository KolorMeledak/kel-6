import ast

class PostfixConverter(ast.NodeVisitor):
    def __init__(self):
        self.output = []

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        self.output.append(self.op_symbol(node.op))

    def visit_Num(self, node):
        self.output.append(str(node.n))

    def visit_Constant(self, node):  # For Python 3.8+
        self.output.append(str(node.value))

    def visit_Name(self, node):
        self.output.append(node.id)

    def op_symbol(self, op):
        return {
            ast.Add: '+',
            ast.Sub: '-',
            ast.Mult: '*',
            ast.Div: '/',
            ast.Pow: '^',
            ast.Mod: '%'
        }[type(op)]

    def generic_visit(self, node):
        if isinstance(node, ast.Expr):
            self.visit(node.value)
        else:
            super().generic_visit(node)

class LinkedListPostfix:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None