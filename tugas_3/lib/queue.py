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
      if self.empty():
         print("Antrian sudah kosong")
         return None

      temp = self.head
      self.head = temp.next
      
      if self.head is None:
         self.tail = None
         
      return temp.data

   def display(self, delimeter=', '):
      if self.empty():
         print("Belum ada data \n")
         return
      
      temp = self.head
      while temp:
         print(temp.data, end=f'{delimeter if temp.next else "\n"}')
         temp = temp.next
      print()
      