# Program Stack dengan Input Dinamis hingga 'stop' dan Proses Pop hingga Error

stack = []
print("Masukkan nama ke dalam stack (ketik 'stop' untuk selesai):")

# Memasukkan elemen ke stack
while True:
    nama = input("Nama: ").strip()
    if nama.lower() == 'stop':
        break
    stack.append(nama)

# Menampilkan hasil stack
print("\nStack saat ini :")
for item in reversed(stack):
      print(item, end='\n')

# Proses pop hingga error
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
