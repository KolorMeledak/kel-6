# KHAIRUL AKMAL
# 1313624017

from to_biner import decimal_to_biner
from to_hexa import decimal_to_hexa
from to_oktal import decimal_to_octal

while True:
   number = input("Masukkan angka: ")
   
   try:
      number = float(number)  
   except ValueError:
      print("Input tidak valid. Harap masukkan angka yang benar (misalnya: 10 atau 10.5).")
      continue

   biner = decimal_to_biner(number)
   print(f"Biner: {biner}")

   print()
   
   octal = decimal_to_octal(number)
   print(f"Oktal: {octal}")

   print()

   hexa = decimal_to_hexa(number)
   print(f"Hexa: {hexa}")
   
   isRepeat = input("Ulang? (y/n): ").lower()
   while isRepeat not in ['y', 'n']:
      print("Input salah.")
      isRepeat = input("Ulang? (y/n): ").lower()

   if isRepeat == 'n':
      break

print("Program konverter selesai.")