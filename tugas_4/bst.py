import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f"membuat root dengan nilai {key}")
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        print(f"{key} dibanding kan dengan {current.value}")
        if key < current.value:
            print(f"{key} < {current.value} → ke kiri")
            if current.left is None:
                current.left = Node(key)
                print(f"Node {key} ditambahkan sebagai anak kiri dari {current.value}\n")
            else:
                self._insert_recursive(current.left, key)
        elif key > current.value:
            print(f"{key} > {current.value} → ke kanan")
            if current.right is None:
                current.right = Node(key)
                print(f"Node {key} ditambahkan sebagai anak kanan dari {current.value}\n")
            else:
                self._insert_recursive(current.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None:
            return False
        if key == current.value:
            return True
        elif key < current.value:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def _calculate_positions(self, node, level=0, x_offset=0, max_depth=1):
        if node is None:
            return

        self._calculate_positions(node.left, level + 1, x_offset - 2**(max_depth - level - 1), max_depth)
        self._calculate_positions(node.right, level + 1, x_offset + 2**(max_depth - level - 1), max_depth)

        node.x = x_offset
        node.y = -level

    def _plot_tree(self, node, ax):
        if node is None:
            return

        if node.left:
            ax.plot([node.x, node.left.x], [node.y, node.left.y], 'k-', lw=1)
            self._plot_tree(node.left, ax)

        if node.right:
            ax.plot([node.x, node.right.x], [node.y, node.right.y], 'k-', lw=1)
            self._plot_tree(node.right, ax)

        ax.text(node.x, node.y, str(node.value), ha='center', va='center', fontsize=10,
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='circle'))

    def display(self):
        if self.root is None:
            print("BST kosong.")
            return

        def _get_depth(node):
            if node is None:
                return 0
            return max(_get_depth(node.left), _get_depth(node.right)) + 1

        max_depth = _get_depth(self.root)

        self._calculate_positions(self.root, max_depth=max_depth)

        fig,ax = plt.subplots(figsize=(10, 6))
        self._plot_tree(self.root, ax)

        ax.set_xlim(-2**max_depth, 2**max_depth)
        ax.set_ylim(-max_depth, 1)
        ax.axis('off')
        plt.title('Binary Search Tree')
        plt.show()

    def preorder_traversal(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def postorder_traversal(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)
        _postorder(self.root)
        return result

    def clear(self):
        self.root = None
        print("BST berhasil dikosongkan.")

bst = BinarySearchTree()

while True:
    print("\n=== MENU BST ===")
    print("1. Tambahkan item")
    print("2. Tapilkan BST")
    print("3. Traversal BST (Preorder, Inorder, Postorder)")
    print("4. Kosongkan BST")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        bulk_input = input("Masukkan data (pisahkan dengan koma (,) jika lebih dari satu): ")
        bulk_list = list(map(lambda bulk_input: bulk_input.strip(), bulk_input.split(', ')))
        for item in bulk_list:
            if bst.search(item):
                print(f"Item {item} sudah ada di dalam BST, dilewati.")
            else:
                bst.insert(item)
        print("Semua data selesai diproses.")
        
    elif pilihan == '2':
        bst.display()

    elif pilihan == '3':
        print(f"Preorder  : {', '.join(bst.preorder_traversal())}")
        print(f"Inorder   : {', '.join(bst.inorder_traversal())}")
        print(f"Postorder : {', '.join(bst.postorder_traversal())}")

    elif pilihan == '4':
        bst.clear()

    elif pilihan == '5':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
