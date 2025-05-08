def print_cities():
   for i, data in enumerate(cities):
      print(data, end=f'{i+1 < len(cities) and " - " or "\n"}')

cities = ['Medan', 'Pontianak', 'Surabaya']

print_cities()
   
option = {
   1: 'Tambah Data',
   2: 'Hapus Data',
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
         cities.append(input("Kota: "))
      case 2:
         print(option[input_user], end='. \n')
         try:
            cities.remove(input("Kota: "))
         except ValueError:
            print("Kota tidak ditemukan")
      case 3:
         print(option[input_user], end='. \n')
         print("Isi array:")
         print_cities()
      case 4:
         print(option[input_user], end='. \n')
         repeat = False
      case _:
         print("Pilihan tidak tersedia")
