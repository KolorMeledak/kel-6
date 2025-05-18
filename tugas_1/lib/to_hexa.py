def decimal_to_hexa(number: int):
    print("Perhitungan Desimal ke Hexa")
    
    if number == 0:
        return "0"
    
    hexa = []

    while number > 0:
        pembagian = number // 16
        sisa = number % 16

        print(f"{number} \t dibagi 16 = {pembagian} sisa {sisa}")
        
        hexa.append(sisa)
        number //= 16
        
    hexa.reverse()
    return ''.join(map(str, hexa))