stack = []

def tambah_data():
    try:
        nama = input("Masukkan nama ke dalam stack: ").strip()
        if not nama:
            raise ValueError("Input tidak boleh kosong.")
        stack.append(nama)
        print(f"{nama} berhasil ditambahkan ke stack.")
    except ValueError as e:
        print(e)

def pop_data():
    if not stack:
        print("Stack kosong")
        return
    nama = input("Masukkan nama yang ingin di-pop: ").strip()
    if nama == stack[-1]:
        removed = stack.pop()
        print(f"{removed} berhasil dihapus dari stack.")
    elif nama in stack:
        print("Nama yang dimasukkan tidak berada pada posisi teratas. Penghapusan dibatalkan.")
    else:
        print("Tidak ada nama yang sesuai pada stack.")

def tampilkan_data():
    if not stack:
        print("Stack kosong")
    else:
        print("Isi stack saat ini:")
        for item in reversed(stack):
            print(item)

while True:
    print("\nMenu:")
    print("1. Tambah data")
    print("2. Pop data (hanya bagian teratas)")
    print("3. Tampilkan data")
    print("4. Selesai")
    pilihan = input("Pilih menu (1/2/3/4): ").strip()
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        pop_data()
    elif pilihan == '3':
        tampilkan_data()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
