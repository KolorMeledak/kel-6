from to_biner import decimal_to_biner
from to_hexa import decimal_to_hexa
from to_oktal import decimal_to_octal

while True:
   number = str(input("Masukkan angka (gunakan angka fixed tanpa koma): "))
   
   if number.isnumeric():
      number = int(number)
   else:
      print("Input yang dimasukkan tidak sesuai format.")
      continue

   biner = decimal_to_biner(number)
   octal = decimal_to_octal(number)
   hexa = decimal_to_hexa(number)

   print("Biner: " + biner)
   print("Oktal: " + octal)
   print("Hexa: " + hexa)
   
   isRepeat = input("Ulang? (y/n): ").lower()
   while isRepeat not in ['y', 'n']:
      print("Input salah.")
      isRepeat = input("Ulang? (y/n): ").lower()

   if isRepeat == 'n':
      break

print("Program konverter selesai.")