kota_list = []

def add(list, item):
    try:
        if any(i == item for i in list):
            print(f"{item} sudah ada di dalam list")
            return list
        if item == "":
            print("Input tidak boleh kosong")
        else:
            list.append(item)
            print(f"{item} berhasil ditambahkan")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Terjadi kesalahan saat menambahkan item")
    return list

def remove(list, item):
    try:
        for i in list:
            if i == item:
                list.remove(i)
                print(f"{item} berhasil dihapus")
                break
        else:
            print(f"{item} tidak ditemukan di dalam list")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Terjadi kesalahan saat menghapus item")
    return list

def search(list, item):
    try:
        if any(i== item for i in list):
            print(f"{item} ditemukan di dalam list")
        else:
            print(f"{item} tidak ditemukan di dalam list")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Terjadi kesalahan saat mencari item")
    return list

def display(list,delimeter =' - '):
    try:
        if len(list) == 0:
            print("List kosong")
        else:
            print("Isi list:")
            print(delimeter.join(list))
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Terjadi kesalahan saat menampilkan list")
    return list

def display_urut(list, delimeter=' - '):
    try:
        if len(list) == 0:
            print("List kosong")
        else:
            print("Isi list (terurut):")
            list_urut = sorted(list)
            print(delimeter.join(list_urut))
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Terjadi kesalahan saat menampilkan list")
    return list

kota_list = ['Medan', 'Pontianak', 'Surabaya']

# Main program
while True:
    option = {
    1: 'Tambah Data',
    2: 'Hapus Data',
    3: 'Cari Data',
    4: 'Tampilkan Data',
    5: 'Selesai'
    }
    print("\n========= Menu Array List =========")
    for i, data in option.items():
      print(f'{i}. {data}')
    
    try:
        pilihan = int(input("Pilih salah satu dari pilihan tersedia (1/2/3/4/5): "))
        if pilihan < 1 or pilihan > 5:
            raise ValueError("Pilihan tidak valid")
    except ValueError as e:
        print(e)
        continue
    
    match pilihan:
        case 1:
            print(option[pilihan], end='. \n')
            kota = input("Kota: ").strip()
            add(kota_list, kota)
        case 2:
            print(option[pilihan], end='. \n')
            kota = input("Kota: ").strip()
            remove(kota_list, kota)
        case 3:
            print(option[pilihan], end='. \n')
            kota = input("Kota: ").strip()
            search(kota_list, kota)
        case 4:
            opsi= {
                1: 'Pengurutan sesuai alfabet',
                2: 'Pengurutan sesuai antrian input'
            }
            for i, data in opsi.items():
                print(f'{i}. {data}')
            match input("Pilih metode pengurutan (1/2): "):
                case '1':
                    display_urut(kota_list)
                case '2':
                    display(kota_list)
                case _:
                    print("Pilihan tidak valid")
        case 5:
            print(option[pilihan], end='. \n')
            break
        case _:
            print("Pilihan tidak tersedia")