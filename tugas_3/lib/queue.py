class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
class Queue:
   def __init__(self):
      self.head = None
      self.tail = None
      
   def empty(self):
      return self.head is None
   
   def push(self, new_data):
      new_node = Node(new_data)
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         self.tail = new_node
   
   def pop(self):
      if self.head is None:
         print("Antrian sudah kosong")
         return None
      else:
         temp = self.head
         self.head = temp.next
         return temp.data
   
   def display(self):
      temp = self.head
      while temp:
         print(temp.data)
         temp = temp.next
      print()
      