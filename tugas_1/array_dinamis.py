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
    cek = True
    while cek:
        print("\nMelakukan proses pop hingga error")
        
        data_input = input("Masukkan nama yang ingin dihapus: ")
        try:
            if data_input == '':
                raise ValueError("Input tidak boleh kosong")
            if not stack:
                raise ValueError("Stack kosong")
            if data_input not in stack:
                raise ValueError(f"Data '{data_input}' tidak ditemukan dalam stack.")
            if data_input != stack[-1]:
                raise ValueError(f"Data '{data_input}' bukan data teratas dalam stack.")
            else:
                stack.remove(data_input)
                
            print(f"{data_input} berhasil dihapus")
        except ValueError as err:   
            print(err)
            print("Ulangi lagi? (y/n): ", end='')
            ulang = input().strip().lower()
            if ulang == 'y':
                continue
            else:
                cek = False
                break
        
    repeat = input("\nUlang apa kagak woi !?!??! (y/n): ").strip().lower() == 'y'
    if not repeat:
        print("Terima kasih telah menggunakan program ini.")
        break
