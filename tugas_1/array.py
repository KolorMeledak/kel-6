stack = []

input = "Indah Putri Cahaya Lestari            , Aminudin, Bahtiar, Cita, Dul, Engel, Farah, Galih, Ambar, Kevin"
# input = str(input("Masukkan nama (beri koma untuk memisahkan): "))
limit = 5

input = list(map(lambda name: name.strip(), input.split(', ')))
stack = input[:limit]

stack_over = input[limit:]

if len(stack_over) > 0: 
   print("Antrian penuh.")
   for name in stack_over:
      print(f'{name} tidak dimasukkan.')

print(stack)
