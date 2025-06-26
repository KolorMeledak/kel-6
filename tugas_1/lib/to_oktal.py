# KHAIRUL AKMAL
# 1313624017

def decimal_to_octal(number: float|int) -> str:
    print("Perhitungan Desimal ke Oktal")
    
    if number == 0 or number == 0.0:
        return "0"
    
    if not number.is_integer():
        return decimal_float_to_octal(number)
    else:
        number = int(number)
    
    octal = []

    while number > 0:
        pembagian = number // 8
        sisa = number % 8

        print(f"{number} \t dibagi 8 = {pembagian} sisa {sisa}")
        
        octal.append(sisa)
        number //= 8
        
    octal.reverse()
    return ''.join(map(str, octal))

def decimal_float_to_octal(number: float) -> str:
    precision = 8  

    # Kalikan dengan 8^8 untuk bisa diolah
    format_number = int(number * (8 ** precision))

    octal_digits = []

    while format_number > 0:
        pembagian = format_number // 8
        sisa = format_number % 8
        
        print(f"{format_number} \t dibagi {8} = {pembagian} sisa {sisa}")
        
        octal_digits.append(sisa)
        format_number = pembagian

    octal_digits.reverse() 

    octal_string = ''.join(map(str, octal_digits))

    if len(octal_string) < 3 + precision:
        octal_string = octal_string.zfill(3 + precision)

    # bila hasil "0045" -> "45"
    integer_part = octal_string[:3].lstrip("0") or "0"
    # ambil 8 digit terakhir
    fraction_part = octal_string[3:3 + precision]

    final_octal = f"{integer_part}.{fraction_part}"
    return final_octal
