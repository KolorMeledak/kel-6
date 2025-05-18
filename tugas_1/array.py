stack = []
limit = 5

def push(inputName):
   if len(stack) >= limit:
      print("Antrian Penuh!")
   else:
      stack.append(inputName)
      print(f"{inputName} berhasil ditambah")

def pop():
   if not stack:
        print("Stack kosong! Tidak ada nama yang bisa dihapus.")
   else:
        nama = stack.pop()
        print(f"{nama} dihapus dari stack.")
        
def display():
   if not stack:
        print("Stack kosong.")
   else:
        print("Isi stack:")
        for i in range(len(stack)-1, -1, -1):
            print(f"{i+1}. {stack[i]}")

while True:
   print("\n========= Menu Stack =========")
   print("1. Push (Tambah Nama)")
   print("2. Pop (Hapus Nama Teratas)")
   print("3. Tampilkan Stack")
   print("4. Update Limit")
   print("5. Keluar")
    
   pilihan = int(input("Masukkan Opsi: "))

   if pilihan == "1":
         nama = input("Masukkan nama: ")
         push(nama)
   elif pilihan == "2":
         pop()
   elif pilihan == "3":
         display()
   elif pilihan == "4":
         inputLimit = int(input("Masukkan Limit Tambahan Baru: "))
         limit += inputLimit
         print(f"limit berhasil di update menjadi {limit}")
   elif pilihan == "5":
         print("Keluar dari program.")
         break
   else:
         print("Opsi tidak valid!")
