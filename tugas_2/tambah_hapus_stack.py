from lib.linkedlist import LinkedList

ll = LinkedList()

option = {
   1: 'Tambah Data',
   2: 'Hapus Data',
   3: 'Cari Data',
   4: 'Tampilkan Data',
   5: 'Selesai'
}

repeat = True
ll.push("Medan")

while repeat:
   print("Menu:")
   for i, data in option.items():
      print(f'{i}. {data}')
   
   input_user = int(input("Pilihan (1, 2, 3, atau 4 dan tekan Enter): "))
   
   match input_user:
      case 1:
         print(option[input_user], end='. \n')
         ll.push(input("Kota: ").strip())
      case 2:
         print(option[input_user], end='. \n')
         try:
            inp = input("Kota: ").strip()
            ll.delete(inp)
            print(f"Data '{inp}' berhasil dihapus")
         except ValueError as err:
            print(err)
      case 3:
         print(option[input_user], end='. \n')
         inp = input("Kota: ").strip()
         data = ll.search(inp)
         if data:
            print("Kota ditemukan:", data)
         else:
            print(f"Kota {inp} tidak ditemukan")
      case 4:
         print(option[input_user], end='. \n')
         print("Isi array:")
         ll.display(delimeter=', ')
      case 5:
         print(option[input_user], end='. \n')
         repeat = False
      case _:
         print("Pilihan tidak tersedia")
