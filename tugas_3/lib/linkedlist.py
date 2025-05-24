class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class LinkedList:
   def __init__(self):
      self.head = None
        
   def empty(self):
      return self.head == None
        
   def push(self, new_data):
      new_node = Node(new_data)
      new_node.next = self.head
      self.head = new_node
        
   def length(self):
      temp = self.head
      count = 0
      while temp:
         count += 1
         temp = temp.next
      return count
   
   def display(self, delimeter=''):
      if self.empty():
         print("Belum ada data \n")
         return
      
      temp = self.head 
      while temp:
         print(temp.data,end=f'{delimeter if temp.next else "\n"}') 
         temp = temp.next 
      print()
   
   def pop(self):
      if self.empty():
         return None
      
      temp = self.head
      self.head = temp.next
      return temp.data
      