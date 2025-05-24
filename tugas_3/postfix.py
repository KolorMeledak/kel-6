import ast
from lib.linkedlistPostfix import PostfixConverter
from lib.linkedlistPostfix import LinkedListPostfix


expr = LinkedListPostfix()

def to_postfix(expr):
    tree = ast.parse(expr, mode='eval')
    converter = PostfixConverter()
    converter.visit(tree.body)
    return ' '.join(converter.output)

repeat = True

while repeat:
    print("===========Postfix Converter===========")
    expr = input("Masukkan operasi matematika: ")
    print("Infix:", expr)
    print("Postfix:", to_postfix(expr))
    choose = input("Apakah anda ingin mengulang kembali? (y/n): ").strip().lower()
    if choose != 'y':
        repeat = False
        print("Terima kasih telah menggunakan Postfix Converter!")
