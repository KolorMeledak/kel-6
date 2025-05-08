def balik_string(teks):
    stack = []

    for char in teks:
        stack.append(char)

    hasil = ''

    while stack:
        hasil += stack.pop()
    return hasil

kalimat = input("Masukkan string yang ingin dibalik: ")
hasil = balik_string(kalimat)
print(f"Hasil balik: {hasil}")
