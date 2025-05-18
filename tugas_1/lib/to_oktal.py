def decimal_to_octal(number: int):
    print("Perhitungan Desimal ke Oktal")
    
    if number == 0:
        return "0"
    
    octal = []

    while number > 0:
        pembagian = number // 8
        sisa = number % 8

        print(f"{number} \t dibagi 8 = {pembagian} sisa {sisa}")
        
        octal.append(sisa)
        number //= 8
        
    octal.reverse()
    return ''.join(map(str, octal))