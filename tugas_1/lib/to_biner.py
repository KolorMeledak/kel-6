def decimal_to_biner(number: int):
    print("Perhitungan Desimal ke Biner")
    
    if number == 0:
        return "0000"
    
    binary_number = []

    while number > 0:
        pembagian = number // 2
        sisa = number % 2

        print(f"{number} \t dibagi 2 = {pembagian} sisa {sisa}")
        
        binary_number.append(sisa)
        number //= 2

    binary_number.reverse()
    binary_number_to_string = ''.join(map(str, binary_number))
    
    return binary_number_to_string.zfill(4)