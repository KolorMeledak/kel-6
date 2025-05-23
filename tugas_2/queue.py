from collections import deque

dq = deque([])

while True:
    try:
        limit = int(input("Masukkan batas maksimal antrian: "))
        if limit > 0:
            break
        else:
            print("Limit harus lebih dari 0.")
    except ValueError:
        print("Masukkan angka yang valid.")

while True:
    print("\nMenu:")
    print("1. Tambah antrian")
    print("2. Hapus antrian (pilih nama)")
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
            print("\nDaftar antrian :")
            for nama in dq:
                print(nama)
            nama_hapus = input("Masukkan nama yang ingin dihapus: ").strip().lower()
            if dq[0].lower() == nama_hapus:
                dq.popleft()
                print(f"{nama_hapus} telah keluar dari antrian.")
            elif nama_hapus in dq:
                print(f"Tidak bisa menghapus {nama_hapus}, karena bukan antrian paling depan.")
            else:
                print(f"{nama_hapus} tidak ada dalam antrian.")
        else:
            print("Antrian kosong.")

    elif pilihan == '3':
        if dq: 
            print("\nDaftar antrian :")
            for nama in dq:
                print(nama)
        else:
            print("Antrian kosong.")

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
