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
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.value:
            if current.right is None:
                current.right = Node(key)
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
    print("2. Cari item")
    print("3. Tampilkan traversal BST (Preorder, Inorder, Postorder)")
    print("4. Kosongkan BST")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        bulk_input = input("Masukkan data (pisahkan dengan spasi jika lebih dari satu): ")
        bulk_list = list(map(int, bulk_input.strip().split()))
        for item in bulk_list:
            if bst.search(item):
                print(f"Item {item} sudah ada di dalam BST, dilewati.")
            else:
                bst.insert(item)
                print(f"Item {item} berhasil ditambahkan ke dalam BST.")
        print("Semua data selesai diproses.")

    elif pilihan == '2':
        item = int(input("Masukkan item yang ingin dicari: "))
        if bst.search(item):
            print(f"Item {item} ditemukan di dalam BST.")
        else:
            print(f"Item {item} tidak ditemukan.")

    elif pilihan == '3':
        print("Preorder Traversal :", bst.preorder_traversal())
        print("Inorder Traversal  :", bst.inorder_traversal())
        print("Postorder Traversal:", bst.postorder_traversal())

    elif pilihan == '4':
        bst.clear()

    elif pilihan == '5':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
