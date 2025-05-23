stack = []

while True:
      limit = int(input("Masukkan batas maksimal stack: "))
      if limit > 0:
            break
      else:
            print("Limit harus lebih dari 0!")

def push(inputName):
      
      if len(stack) >= limit:
            print("Antrian Penuh!")
      else:
            stack.append(inputName)
            print(f"{inputName} berhasil ditambah")

def pop():
   if not stack:
      print("Stack kosong! Nggak ada nama yang bisa dihapus.")
   else:
      nama = stack.pop()
      print(f"{nama} dihapus dari stack.")
        
def display():
   if not stack:
      print("Stack kosong.")
   else:
      print("Isi stack:")
      for i in reversed(range(len(stack))):
            print(stack[i])
repeat = True
while repeat: 
    while True:
        nama = input("Masukkan nama (pisahkan dengan koma ",")")
        nama = list(map(lambda name: name.strip(), input.split(', ')))
        push(nama)
    
    print("\nProses pop:")

i = 1
while True:
    try:
        print(f"Pop ke ({i}): {stack.pop()}")
        i += 1
    #bagian ini untuk menangani error jika stack kosong
    except IndexError:
        print("Stack kosong, tidak ada yang bisa di pop.")
        print("*error* (stack kosong)")
        break
    

    repeat = input("\nUlang apa kagak woi !?!??! (y/n): ").strip().lower() == 'y'
    if not repeat:
        print("Terima kasih telah menggunakan program ini.")
        break