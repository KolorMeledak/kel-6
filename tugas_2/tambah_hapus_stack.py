from lib.linkedlist import LinkedList

ll = LinkedList()

ll.push("Medan")
ll.push("Pontianak")
ll.push("Surabaya")

option = {
   1: 'Tambah Data',
   2: 'Hapus Data',
   3: 'Cari Data',
   4: 'Tampilkan Data',
   5: 'Selesai'
}

repeat = True
while repeat:
   print("Menu:")
   for i, data in option.items():
      print(f'{i}. {data}')
   
   input_user = int(input("Pilihan (1, 2, 3, 4, atau 5 dan tekan Enter): "))
   
   match input_user:
      case 1:
         print(option[input_user], end='. \n')
         kota = input("Kota: ").strip()
         ll.push(kota)
         ll.sort()  # Ensure the linked list is sorted after each push
      case 2:
         print(option[input_user], end='. \n')
         try:
            inp = input("Kota: ").strip()
            if inp == '':
               raise ValueError("Input tidak boleh kosong")
            if ll.empty():
               raise ValueError("Linked List kosong")
            ll.delete(inp)
            print(f"Kota {inp} berhasil dihapus")
         except ValueError as err:
            print(err)
      case 3:
         print(option[input_user], end='. \n')
         inp = input("Kota: ").strip()
         if inp == '':
            print("Input tidak boleh kosong")
            continue
         data = ll.search(inp)
         if data:
            print(f"Kota {inp} ditemukan:")
         else:
            print(f"Kota {inp} tidak ditemukan")
      case 4:
         print(option[input_user], end='. \n')
         print("Isi array:")
         ll.display(delimeter=' - ')
      case 5:
         print(option[input_user], end='. \n')
         repeat = False
      case _:
         print("Pilihan tidak tersedia")
