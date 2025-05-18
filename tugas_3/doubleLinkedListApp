from lib.doublyLinkedList import DoublyLinkedList


senarai = DoublyLinkedList()

while True:
    print("0. Keluar dari Program")
    print("1. Tambahkan Data Awal")
    print("2. Tambahkan Data Baru Setelah Kunci")
    print("3. Tambahkan Data Akhir")
    print("4. Hapus Data Awal")
    print("5. Hapus Data Setelah Kunci")
    print("6. Hapus Data Akhir")
    print("7. Tampilkan Data Dari Depan")
    print("8. Tampilkan Data Dari Belakang")
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
                senarai.insertFirst(data)
                
            print(f"Isi setelah {banyakData} dimasukkan :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 2):   
        banyakData = int(input("Masukkan banyak data: "))
        key = input("Masukkan Data Di List Sebagai Kunci (Data Baru akan Ditambah Setelah Data Sebagai Kunci Tersebut): ")
        if banyakData == 0:
            break
        else:
            for i in range (banyakData):
                data = input("Masukkan data ke-" + str(i+1) + ": ")
                senarai.insertAfter(key, data)
                
            print(f"Isi setelah {banyakData} dimasukkan :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 3):   
        banyakData = int(input("Masukkan banyak data: "))
        if banyakData == 0:
            break
        else:
            for i in range(banyakData):
                data = input("Masukkan data ke-" + str(i+1) + ": ")
                senarai.insertLast(data)
                
            print(f"Isi setelah {banyakData} dimasukkan :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 4):
        if senarai.isEmpty():
            print("Data Kosong, Tidak Bisa Melakukan Penghapusan")
        else:
            data = senarai.removeFirst()
            print(f"Isi setelah {data} dihapus :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 5):
        if senarai.isEmpty():
            print("Data Kosong, Tidak Bisa Melakukan Penghapusan")
        else:
            key = input("Masukkan Data Di List Sebagai Kunci (Data Setelah Data Kunci Tersebut Akan Dihapus):  ")
            data = senarai.removeAfterKey(key)
            print(f"Isi setelah {data} dihapus :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 6):
        if senarai.isEmpty():
            print("Data Kosong, Tidak Bisa Melakukan Penghapusan")
        else:
            data = senarai.removeLast()
            print(f"Isi setelah {data} dihapus :")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 7):
        if senarai.isEmpty():
            print("Data Masih Kosong")
        else:
            print("List Data Sekarang Dari Depan Ke Belakang: ")
            senarai.displayForward()
            print("-"*20)
    elif (opsi == 8):
        if senarai.isEmpty():
            print("Data Masih Kosong")
        else:
            print("List Data Sekarang Dari Belakang Ke Depan: ")
            senarai.displayBackward()
            print("-"*20)
    else:
        print("Opsi tidak tersedia")
        print("-"*20)
        break
