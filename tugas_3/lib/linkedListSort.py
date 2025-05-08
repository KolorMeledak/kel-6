class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class Sortlist:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        newNode = Node(data)
        newNode.next = None
        prev = None
        cur = self.head

        while cur is not None and data > cur.data:
            prev = cur
            cur = cur.next
        
        if prev == None:
            self.head = newNode
        else:
            prev.next = newNode
        
        newNode.next = cur
        
    def isEmpty(self):
        return self.head == None
    
    def remove(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
        
    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next