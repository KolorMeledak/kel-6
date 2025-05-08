from lib.linkedListSort import Sortlist

senarai = Sortlist()
while True:
    print("0. Keluar dari Program")
    print("1. Tambahkan Data Awal")
    print("2. Hapus Data")
    opsi = int (input("Pilih Opsi: "))
    
    if (opsi == 0):
        print("Terima Kasih")
        break
    elif (opsi == 1):   
        banyakData = int(input("Masukkan banyak data: "))
        if banyakData == 0:
            break
        else:
            for i in range(banyakData):
                data = input("Masukkan data ke-" + str(i+1) + ": ")
                senarai.insert(data)
                
            print(f"Isi setelah {banyakData} dimasukkan :")
            senarai.display()
    elif (opsi == 2):
        if senarai.isEmpty():
            print("Data Kosong")
        else:
            data = senarai.remove()
            print(f"Isi setelah {data} dihapus :")
            senarai.display()
    else:
        print("Opsi tidak tersedia")
        break

    