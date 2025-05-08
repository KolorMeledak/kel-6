from collections import deque

dq = deque([])
limit = 5

while True:
    print("\nMenu:")
    print("1. Tambah antrian")
    print("2. Hapus antrian paling depan")
    print("3. Lihat antrian")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        if len(dq) < limit:
            nama = input("Masukkan nama: ").strip()
            dq.append(nama)
            print(f"{nama} berhasil ditambahkan ke antrian.")
        else:
            print("Antrian penuh.")

    elif pilihan == '2':
        if dq:
            keluar = dq.popleft()
            print(f"{keluar} telah keluar dari antrian.")
        else:
            print("Antrian kosong.")

    elif pilihan == '3':
        if dq: 
            print(f"Daftar antrian: {', '.join(dq)}")
        else:
            print("Antrian kosong.")

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
