def balik_string(teks):
    stack = []

    for char in teks:
        stack.append(char)

    hasil = ''

    while stack:
        hasil += stack.pop()
    return hasil

while True:
    print("Masukkan teks (paragraf dipisah oleh 1 baris kosong, tekan Enter 3x untuk selesai):")
    paragraf_list = []
    paragraf = []

    while True:
        baris = input()
        if baris == '':
            if paragraf:
                    paragraf_list.append('\n'.join(paragraf))
                    paragraf = []                        
            else:
                break 
        else:
            paragraf.append(baris)

    if not paragraf_list:
        print("Tidak ada teks yang dimasukkan. Silakan coba lagi.")

    else:
        reverse_paragraf = []
        for p in paragraf_list:
            reverse_paragraf.append(balik_string(p))

        hasil_akhir = '\n\n'.join(reverse_paragraf).strip()
        print(f"Hasil balik:\n{hasil_akhir}")

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