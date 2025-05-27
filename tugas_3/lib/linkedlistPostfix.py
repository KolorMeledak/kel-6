# import ast

# class PostfixConverter(ast.NodeVisitor):
#     def __init__(self):
#         self.output = []

#     def visit_BinOp(self, node):
#         self.visit(node.left)
#         self.visit(node.right)
#         self.output.append(self.op_symbol(node.op))

#     def visit_Num(self, node):
#         self.output.append(str(node.n))

#     def visit_Constant(self, node):  # For Python 3.8+
#         self.output.append(str(node.value))

#     def visit_Name(self, node):
#         self.output.append(node.id)

#     def op_symbol(self, op):
#         return {
#             ast.Add: '+',
#             ast.Sub: '-',
#             ast.Mult: '*',
#             ast.Div: '/',
#             ast.Pow: '^',
#             ast.Mod: '%'
#         }[type(op)]

#     def generic_visit(self, node):
#         if isinstance(node, ast.Expr):
#             self.visit(node.value)
#         else:
#             super().generic_visit(node)
    
    
            


# class LinkedListPostfix:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head is None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def pop(self):
#         if self.is_empty():
#             return None
#         data = self.head.data
#         self.head = self.head.next
#         return data

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=' ')
#             current = current.next
#         print()
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListPostfix:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]  # Reverse to get correct order

def operasi(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    output = LinkedListPostfix()
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        if expression[i].isalnum():
            j = i
            while j < len(expression) and (expression[j].isalnum() or expression[j] == '.'):
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            tokens.append(expression[i])
            i += 1

    for token in tokens:
        if token.isalnum() or '.' in token:
            output.push(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.push(stack.pop())
            stack.pop()  # Remove '('
        else:
            while (stack and operasi(stack[-1]) >= operasi(token)):
                output.push(stack.pop())
            stack.append(token)
    while stack:
        output.push(stack.pop())
    return output.to_list()