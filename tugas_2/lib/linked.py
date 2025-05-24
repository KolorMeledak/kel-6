class Node: 
    def __init__(self, kode, nama): 
        self.kode = kode
        self.nama = nama
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None #head for the first node
        
    def insert(self, kode, nama):
        new_node = Node(kode, nama)
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next 
        temp.next = new_node

    def display(self):
        temp = self.head 
        while temp: 
            print(f"{temp.kode} = {temp.nama}")
            temp = temp.next
        
    def search(self, key):
        temp = self.head
        found = False

        while temp:
            if temp.kode == key or temp.nama == key:
                print("\nData ditemukan:")
                print(f"{temp.kode} = {temp.nama}")
                found = True
            temp = temp.next

        if not found:
            print(f"Data '{key}' tidak ditemukan.")


    def delete(self, key):
        temp = self.head
        prev = None
        
        if temp and (temp.kode == key or temp.nama == key):
            self.head = temp.next
            temp = None
            print(f"Data {key} berhasil dihapus")
            return
        
        while temp and (temp.kode != key and temp.nama != key):
            prev = temp
            temp = temp.next
        
        if temp is None:
            print(f"Data {key} tidak ditemukan")
            return 
        
        prev.next = temp.next
        temp = None 
        print(f"Data {key} berhasil dihapus")
        return