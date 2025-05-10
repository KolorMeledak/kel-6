from lib.linkedlist import LinkedList

tumpukan = LinkedList()   
option = {
   1: 'Tambah Data',
   2: 'Ambil Data',
   3: 'Tampilkan Data',
   4: 'Selesai'
}

repeat = True
while repeat:
   print("Menu:")
   for i, data in option.items():
      print(f'{i}. {data}')
   
   input_user = int(input("Pilihan (1, 2, 3, atau 4 dan tekan Enter): "))
   
   match input_user:
      case 1:
         print(option[input_user], end='. \n')
         tumpukan.push(input("Masukkan data: ").strip())
      case 2:
         print(option[input_user], end='. \n')
         terambil = tumpukan.pop()
         if terambil is None:
            print("Antrian sudah kosong")
            continue
         
         print(f"Data '{terambil}' berhasil diambil")
      case 3:
         print(option[input_user], end='. \n')
         print("Isi array:")
         tumpukan.display(delimeter=', ')
      case 4:
         print(option[input_user], end='. \n')
         repeat = False
      case _:
         print("Pilihan tidak tersedia")