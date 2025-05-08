from lib.queue import Queue

ll = Queue()
ll.push("A")
ll.push("B")
ll.push("C")
ll.push("D")
print("Antrian semula")
ll.display()

print("Data yang dipanggil pertama")
print(ll.pop())
   
print('Antrian setelah dipanggil')
ll.display()

ll.push("X")
ll.push("Y")

print("Isi antrian setelah penambahan dua data:");
ll.display()