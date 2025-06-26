from collections import deque

list_antrian = deque()
antrian_dibatasi = []

while True:
    print("\n===== MENU =====")
    print("1. Tambah antrian")
    print("2. Hapus antrian (pilih nama)")
    print("3. Lihat antrian")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        while True:
            print("\nPilih metode input:")
            print("1. Input satu per satu")
            print("2. Input sekaligus (pisahkan dengan koma)")
            metode_input = input("Pilih (1/2): ").strip()

            if metode_input == '1':
                while True:
                    nama = input("Masukkan nama (atau langsung tekan enter untuk berhenti): ").strip()
                    if nama == '':
                        print("Input selesai.")
                        break
                    list_antrian.append(nama)
                    print(f"{nama} berhasil ditambahkan ke antrian.\n")
                break  # keluar dari metode input setelah selesai

            elif metode_input == '2':
                nama_banyak = input("Masukkan beberapa nama, pisahkan dengan koma: ").strip()
                if nama_banyak:
                    daftar_nama = [n.strip() for n in nama_banyak.split(',') if n.strip()]
                    for nama in daftar_nama:
                        list_antrian.append(nama)
                        print(f"{nama} berhasil ditambahkan ke antrian.")
                else:
                    print("Tidak ada nama yang dimasukkan.")
                break  # keluar dari metode input setelah selesai

            else:
                print("Pilihan tidak valid. Coba lagi.")


    elif pilihan == '2':
        if list_antrian:
            print("\nDaftar antrian :")
            for nama in list_antrian:
                print(nama)
            nama_hapus = input("Masukkan nama yang ingin dihapus (harus yang paling depan): ").strip()
            if list_antrian[0].lower() == nama_hapus.lower():
                list_antrian.popleft()
                print(f"{nama_hapus} telah keluar dari antrian.")
            elif nama_hapus.lower() in (n.lower() for n in list_antrian):
                print(f"Tidak bisa menghapus {nama_hapus}, karena bukan antrian paling depan.")
            else:
                print(f"{nama_hapus} tidak ada dalam antrian.")
        else:
            print("Antrian kosong.")

    elif pilihan == '3':
        print("\nPilih bentuk antrian :")
        print("1. Antrian biasa")
        print("2. Antrian dibatasi")
        bentuk_antrian = input("Pilih bentuk antrian (1-2): ")
        
        if bentuk_antrian == '1':
            if list_antrian:
                print("\nDaftar antrian :")
                for i in list_antrian:
                    print(i)
            else:
                print("Antrian kosong.")

        elif bentuk_antrian == '2':
            if not list_antrian:
                print("Antrian kosong.")
                continue

            while True:
                try:
                    limit = int(input("Masukkan batas maksimal antrian:"))
                    if limit > 0:
                        break
                    else:
                        print("Limit harus lebih dari 0.")
                except ValueError:
                    print("Masukkan angka yang valid.")

            antrian_dibatasi.clear()  # clear sebelumnya biar nggak numpuk
            print("\n")
            for i in list_antrian:
                if len(antrian_dibatasi) < limit:
                    print(f"{i} berhasil ditambahkan ke antrian.")
                    antrian_dibatasi.append(i)
                else:
                    print(f"antrian penuh, {i} tidak ditambahkan karena antrian penuh.")

            print("\nDaftar antrian :")
            for i in antrian_dibatasi:
                print(i)
            
            if len(antrian_dibatasi) < limit:
                print(f"\nmasih ada {limit - len(antrian_dibatasi)} antrian kosong")

        else:
            print("Pilihan tidak valid.")

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
