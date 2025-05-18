stack = []

while True:
    try:
      limit = int(input("Masukkan batas maksimal stack: "))
      if limit > 0:
            break
      else:
            print("Limit harus lebih dari 0!")
    except ValueError:
            print("Input harus berupa angka ya")

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

while True:
   print("\n========= Menu Stack =========")
   print("1. Push (Tambah Nama)")
   print("2. Pop (Hapus Nama Teratas)")
   print("3. Tampilkan Stack")
   print("4. Keluar")
    
   pilihan = int(input("Masukkan Opsi: "))

   if pilihan == 1:
         limit = int(input("Masukkan Maks Data: "))
         nama = input("Masukkan nama: ")
         push(nama)
   elif pilihan == 2:
         pop()
   elif pilihan == 3:
         display()
   elif pilihan == 4:
         print("Keluar dari program.")
         break
   else:
         print("Pilihan tidak valid!")
