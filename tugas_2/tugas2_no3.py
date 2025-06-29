kota_list = []

option = {
   1: 'Tambah Data',
   2: 'Hapus Data',
   3: 'Cari Data',
   4: 'Tampilkan Data (Urutan Stack)',
   5: 'Tampilkan Data (Terurut)',
   6: 'Selesai'
}

repeat = True
while repeat:
   print("\nMenu:")
   for i, data in option.items():
      print(f'{i}. {data}')
   
   try:
      input_user = int(input("Pilihan (1-6): "))
   except ValueError:
      print("Input harus angka!")
      continue

   match input_user:
      case 1:
         print(option[input_user])
         kota = input("Kota: ").strip()
         if kota:
            kota_list.append(kota)
            print(f"Kota {kota} berhasil ditambahkan")
         else:
            print("Input tidak boleh kosong")
      case 2:
         print(option[input_user])
         kota = input("Kota yang ingin dihapus: ").strip()
         if kota_list and kota_list[-1] == kota:
            kota_list.pop()
            print(f"Kota {kota} berhasil dihapus dari urutan paling atas stack")
         else:
            print(f"Kota {kota} hanya dapat dihapus jika berada di urutan paling atas stack")
      case 3:
         print(option[input_user])
         kota = input("Kota yang dicari: ").strip()
         if kota in kota_list:
            print(f"Kota {kota} ditemukan sebanyak {kota_list.count(kota)} kali")
         else:
            print(f"Kota {kota} tidak ditemukan")
      case 4:
         print(option[input_user])
         if kota_list:
            print("Data (urutan stack):")
            print(' - '.join(kota_list))
         else:
            print("Data kosong")
      case 5:
         print(option[input_user])
         if kota_list:
            print("Data (terurut):")
            print(' - '.join(sorted(kota_list)))
         else:
            print("Data kosong")
      case 6:
         print(option[input_user])
         repeat = False
      case _:
         print("Pilihan tidak tersedia")
