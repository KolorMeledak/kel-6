# KHAIRUL AKMAL
# 1313624017

from linked import LinkedList

ll = LinkedList()

def assign():
    print("Masukkan kode dan nama sesuai dengan ketentuannya (Ex: AF, Aminudin Fikri)")
    print("Masukkan kata 'selesai' untuk mengakhiri\n")

    while True:
        inputan = input().strip()
        if inputan.lower() == 'selesai':
            break
        try:
            inisial, nama = list(map(lambda name: name.strip(), inputan.split(','))) 
            inisial = inisial.upper()
            ll.insert(inisial, nama)
            print(f"Data {inisial}, {nama} berhasil ditambahkan.")
        except ValueError:
            print("Format salah! Gunakan format: INISIAL, Nama Panjang (Ex. AF, Aminudin Fikri)")

def remove():
    inputan = input("Masukkan kode yang perlu dihapus: ")
    inputan = inputan.upper()
    isDelete = ll.delete(f"{inputan}")
    
    if isDelete is None:
        print(f"Data {inputan} tidak ditemukan.")
        return
    else:
        print(f"Data {inputan} berhasil dihapus.")
        return
    
def search():
    inputan = str(input("Masukkan kode yang ingin dicari = "))
    inputan = inputan.upper()
    
    data =ll.search(f"{inputan}")
    if data is not None:
        print(f"Data ditemukan: {data.kode} = {data.nama}")
        return
    else:
        print(f"Data {inputan} tidak ditemukan.")
        return
    
ll.display()

retry = True
while retry:
    pilihan = {
    1: 'Tambah Data',
    2: 'Hapus Data',
    3: 'Pencarian Data',
    4: 'Tampilkan Data',
    5: 'Selesai'
    }
    
    
    print("Menu:")
    for i, data in pilihan.items():
        print(f'{i}. {data}')
    
    option = int(input("Pilih salah satu dari pilihan tersedia (1/2/3/4/5) "))
    
    match option:
        case 1:
            print(pilihan[option], end='. \n')
            assign()
            print()
        case 2:
            print(pilihan[option], end='. \n')
            remove()
            print()
        case 3:
            print(pilihan[option], end='. \n')
            search()
            print()
        case 4:
            data = ll.display()
            if data is not None:
                print()
                continue
                
            print("Linked List masih kosong")
            print()
        case 5:
            retry = False
        case _:
            print("Pilihan tidak tersedia", end='\n\n')