from lib.linkedlist import LinkedList

ll = LinkedList()
ll.push("A")
ll.push("B")
ll.push("C")
ll.push("D")
ll.display()

while not ll.empty():
   print(ll.pop())
   
ll.display()