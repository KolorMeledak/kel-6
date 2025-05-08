from collections import deque

dq = deque([])

input = str(input("Masukkan nama (beri koma untuk memisahkan): "))
limit = 5

# input = input.split(', ')
input = list(map(lambda name: name.strip(), input.split(', ')))

for name in input:
   if len(dq) < limit:
      dq.append(name.strip())
   else:
      print('Antrian penuh.')
      print(f'{name} tidak dimasukkan.')

print(dq)