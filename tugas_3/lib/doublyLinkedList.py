class Doublenode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
        
        
    def insertFirst(self, data):
        newNode = Doublenode(data)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else :
            self.head.prev = newNode
            newNode.next = self.head    
        
        newNode.prev = None
        self.head = newNode
        
    def insertLast(self, data):
        newNode = Doublenode(data)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        newNode.next = None
        self.tail = newNode
        
    def insertAfter(self, key, data):
        find = False
        keyNode = self.head
        while keyNode != None:
            if keyNode.data == key:
                find = True
                break
            keyNode = keyNode.next
        
        if not find:
            return False
        
        newNode = Doublenode(data)
        
        if keyNode == self.tail:
            newNode.next = None
            newNode.prev = self.tail
            self.tail = newNode
        else:
            newNode.next = keyNode.next
            newNode.prev = keyNode
            
        keyNode.next.prev = newNode
        keyNode.next = newNode
        
    def removeFirst(self):
        if self.isEmpty():
            print("List Sudah Kosong")
        
        delete = self.head
        self.head = self.head.next
        self.head.prev = None
        del delete
        
        
    def removeLast(self):
        if self.isEmpty():
            print("List Sudah Kosong")
            
        delete = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del delete
        
    def removeAfterKey(self, key):
        find = False
        keyNode = self.head
        while keyNode is not None:
            if keyNode.data == key:
                find = True
                break
            keyNode = keyNode.next
        
        if not find:
            return False
        
        delete = keyNode.next
        temp = delete.next
        keyNode.next = temp
        temp.prev = keyNode
        del delete 
            
    
    def displayForward(self):
        keyNode = self.head
        while keyNode is not None:
            print(keyNode.data)
            keyNode = keyNode.next

    def displayBackward(self):
        keyNode = self.tail
        while keyNode is not None:
            print(keyNode.data)
            keyNode = keyNode.prev
