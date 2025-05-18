def balik_string(teks):
    stack = []

    for char in teks:
        stack.append(char)

    hasil = ''

    while stack:
        hasil += stack.pop()
    return hasil

while True:
    kalimat = input("Masukkan string yang ingin dibalik: ")
    hasil = balik_string(kalimat)
    print(f"Hasil balik: {hasil}")
    
    while True:
        print("\nApakah Anda ingin mengulang program? (y), atau selesai (n)")
        ulang = input().lower()
        if ulang == 'y':
            print("Program akan diulang.")
            break
        elif ulang == 'n':
            print("Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
        
