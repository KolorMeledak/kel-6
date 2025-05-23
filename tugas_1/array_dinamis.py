repeat = True
# Program Stack dengan Input Dinamis hingga 'stop' dan Proses Pop hingga Error
while repeat:
        
    stack = []
    print("Masukkan nama ke dalam stack (ketik 'stop' untuk selesai):")

    # Memasukkan elemen ke stack
    k = 1
    while True:
        print(f"Nama ke-{k}: ", end='')
        try:
            nama = input().strip()
            if not nama:
                raise ValueError("Input tidak boleh kosong.")
            k += 1
            if nama.lower() == 'stop':
                break
            stack.append(nama)
        except ValueError as e:
            print(e)

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
    
    repeat = input("\nUlang apa kagak woi !?!??! (y/n): ").strip().lower() == 'y'
    if not repeat:
        print("Terima kasih telah menggunakan program ini.")
        break
