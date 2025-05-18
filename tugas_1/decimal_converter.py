from lib.to_biner import decimal_to_biner
from lib.to_hexa import decimal_to_hexa
from lib.to_oktal import decimal_to_octal

while True:
   number = str(input("Masukkan angka (gunakan angka fixed tanpa koma): "))
   
   if number.isnumeric():
      number = int(number)
   else:
      print("Input yang dimasukkan tidak sesuai format.")
      continue

   biner = decimal_to_biner(number)
   print("Biner: " + biner)

   print()
   
   octal = decimal_to_octal(number)
   print("Oktal: " + octal)

   print()

   hexa = decimal_to_hexa(number)
   print("Hexa: " + hexa)
   
   isRepeat = input("Ulang? (y/n): ").lower()
   while isRepeat not in ['y', 'n']:
      print("Input salah.")
      isRepeat = input("Ulang? (y/n): ").lower()

   if isRepeat == 'n':
      break

print("Program konverter selesai.")