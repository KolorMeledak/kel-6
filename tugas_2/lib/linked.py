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
            return True
        
        temp = self.head
        while temp.next:
            temp = temp.next 
        temp.next = new_node
        return True

    def display(self):
        if self.head is None:
            return None
        
        temp = self.head 
        while temp: 
            print(f"{temp.kode} = {temp.nama}")
            temp = temp.next
            return True
        
    def search(self, key):
        temp = self.head
        found = False

        while temp:
            if temp.kode == key or temp.nama == key:
                return temp
            temp = temp.next

        if not found:
            return None


    def delete(self, key):
        temp = self.head
        
        if temp and (temp.kode == key or temp.nama == key):
            self.head = temp.next
            temp = None
            return True
        
        while temp and (temp.kode != key and temp.nama != key):
            temp = temp.next
        
        if temp is None:
            return None