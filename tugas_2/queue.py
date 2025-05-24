from collections import deque

list_antrian = deque([])

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
        if len(list_antrian) < limit:
            while len(list_antrian) < limit:
                nama = input("Masukkan nama (atau langsung tekan enter untuk berhenti): ").strip()
                if nama.lower() == '':
                    print("Input selesai.")
                    break
                list_antrian.append(nama)
                print(f"{nama} berhasil ditambahkan ke antrian.\n")
                
            if len(list_antrian) >= limit:
                print("Antrian sudah penuh.")
        else:
            print("Antrian penuh.")

    elif pilihan == '2':
        if list_antrian:
            print("\nDaftar antrian :")
            for nama in list_antrian:
                print(nama)
            nama_hapus = input("Masukkan nama yang ingin dihapus: ").strip().lower()
            if list_antrian[0].lower() == nama_hapus:
                list_antrian.popleft()
                print(f"{nama_hapus} telah keluar dari antrian.")
            elif nama_hapus in list_antrian:
                print(f"Tidak bisa menghapus {nama_hapus}, karena bukan antrian paling depan.")
            else:
                print(f"{nama_hapus} tidak ada dalam antrian.")
        else:
            print("Antrian kosong.")

    elif pilihan == '3':
        if list_antrian: 
            print("\nDaftar antrian :")
            for nama in list_antrian:
                print(nama)
        else:
            print("Antrian kosong.")

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
