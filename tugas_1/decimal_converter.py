from to_biner import decimal_to_biner
from to_hexa import decimal_to_hexa
from to_oktal import decimal_to_octal

number = str(input("Masukkan angka: "))

biner = decimal_to_biner(number)
octal = decimal_to_octal(number)
hexa = decimal_to_hexa(number)

print("Biner: " + biner)
print("Oktal: " + octal)
print("Hexa: " + hexa)
