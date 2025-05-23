class Node: 
    def __init__(self, kode, nama): 
        self.kode = kode
        self.nama = nama
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None
        
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

        while temp:
            if temp.kode == key or temp.nama == key:
                return temp
            temp = temp.next

        return None


    def delete(self, key):
        temp = self.head
        
        if temp and (temp.kode == key or temp.nama == key):
            self.head = temp.next
            temp = None
            return True
        
        while temp and (temp.kode != key or temp.nama != key):
            temp = temp.next
        
        if temp is None:
            return None