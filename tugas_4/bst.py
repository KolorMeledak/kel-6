from fractions import Fraction
from collections import deque
import shutil

class Node:
    def __init__(self, key_str, key_value):
        self.left = None
        self.right = None
        self.key_str = key_str
        self.key_value = key_value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key_str):
        key_value = self._convert_to_number(key_str)
        if key_value is None:
            print(f"Input {key_str} tidak valid, dilewati.")
            return
        if self.root is None:
            self.root = Node(key_str, key_value)
        else:
            self._insert_recursive(self.root, key_str, key_value)

    def _insert_recursive(self, current, key_str, key_value):
        if key_value < current.key_value:
            if current.left is None:
                current.left = Node(key_str, key_value)
            else:
                self._insert_recursive(current.left, key_str, key_value)
        elif key_value > current.key_value:
            if current.right is None:
                current.right = Node(key_str, key_value)
            else:
                self._insert_recursive(current.right, key_str, key_value)
        else:
            print(f"{key_str} sudah ada, dilewati.")

    def _convert_to_number(self, value):
        try:
            if '/' in value:
                return float(Fraction(value))
            elif '.' in value:
                return float(value)
            else:
                return float(int(value))
        except ValueError:
            return None

    def display_tree(self):
        if not self.root:
            print("BST kosong.")
            return

        max_depth = self._get_depth(self.root)
        terminal_width = shutil.get_terminal_size().columns
        space_unit = 3  # jarak antar node

        root_pos = terminal_width // 2

        queue = deque()
        queue.append((self.root, 0, root_pos))

        levels = {}
        node_refs = {}

        while queue:
            node, depth, pos = queue.popleft()
            if depth not in levels:
                levels[depth] = []
                node_refs[depth] = []
            levels[depth].append((pos, node.key_str))
            node_refs[depth].append((pos, node))

            offset = max(2, int(space_unit * (2 ** (max_depth - depth - 1))))
            offset = min(offset, 20)

            if node.left:
                queue.append((node.left, depth + 1, pos - offset))
            if node.right:
                queue.append((node.right, depth + 1, pos + offset))

        last_depth = max(levels.keys())
        for d in range(0, last_depth + 1):
            line = [" "] * terminal_width
            branches = [" "] * terminal_width
            for pos, val in levels[d]:
                idx = max(0, min(terminal_width - len(val), pos - len(val)//2))
                for i, c in enumerate(val):
                    if 0 <= idx+i < terminal_width:
                        line[idx+i] = c

            if d < last_depth:
                for pos, node in node_refs[d]:
                    if node.left:
                        if pos-1 >= 0:
                            branches[pos-1] = "/"
                    if node.right:
                        if pos+1 < terminal_width:
                            branches[pos+1] = "\\"
            print("".join(line))
            if d < last_depth:
                print("".join(branches))

    def _get_depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_depth(node.left), self._get_depth(node.right))

    def preorder_traversal(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node.key_str)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key_str)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def postorder_traversal(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.key_str)
        _postorder(self.root)
        return result

    def clear(self):
        self.root = None
        print("BST berhasil dikosongkan.")

# Main Program
bst = BinarySearchTree()

while True:
    print("\n=== MENU BST ===")
    print("1. Tambahkan item")
    print("2. Tampilkan BST")
    print("3. Tampilkan Traversal (Preorder, Inorder, Postorder)")
    print("4. Kosongkan BST")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        bulk_input = input("Masukkan data (pisahkan koma): ")
        bulk_list = [x.strip() for x in bulk_input.split(',') if x.strip() != '']

        for item in bulk_list:
            bst.insert(item)
        print("Data selesai.")

    elif pilihan == '2':
        bst.display_tree()

    elif pilihan == '3':
        print(f"\nPreorder  : {', '.join(bst.preorder_traversal())}")
        print(f"Inorder   : {', '.join(bst.inorder_traversal())}")
        print(f"Postorder : {', '.join(bst.postorder_traversal())}")

    elif pilihan == '4':
        bst.clear()

    elif pilihan == '5':
        print("Keluar program.")
        break

    else:
        print("Pilihan tidak valid.")
