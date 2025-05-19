def decimal_to_hexa(number: float|int) -> str:
    print("Perhitungan Desimal ke Hexa")
    
    if number == 0 or number == 0.0:
        return "0"

    if not float(number).is_integer():
        return decimal_float_to_hexa(number) 
    else:
        number = int(number)

    hexa = []

    while number > 0:
        pembagian = number // 16
        sisa = number % 16

        print(f"{number} \t dibagi 16 = {pembagian} sisa {sisa}")
        digit = decimal_to_hex_digit(sisa)
        
        hexa.append(digit)
        number = pembagian

    hexa.reverse()
    return ''.join(hexa)

def decimal_float_to_hexa(number: float) -> str:
    precision = 8
    
    # Kalikan dengan 16^8 untuk bisa diolah
    scaled_number = int(number * (16 ** precision))

    hexa_digits = []

    print("\nProses Konversi Desimal ke Heksadesimal (Manual):")
    while scaled_number > 0:
        quotient = scaled_number // 16
        remainder = scaled_number % 16

        digit = decimal_to_hex_digit(remainder)
        print(f"{scaled_number} \t dibagi {16} = {quotient} sisa {digit}")

        hexa_digits.append(digit)
        scaled_number = quotient

    hexa_digits.reverse()

    if len(hexa_digits) < 3 + precision:
        hexa_digits = ['0'] * (3 + precision - len(hexa_digits)) + hexa_digits

    # "00ABC" -> "ABC"
    integer_part = ''.join(hexa_digits[:3]).lstrip('0') or '0'
    fractional_part = ''.join(hexa_digits[3:3 + 8])

    return f"{integer_part}.{fractional_part}"


def decimal_to_hex_digit(value: int) -> str:
    if 0 <= value <= 9:
        return str(value)
    elif 10 <= value <= 15:
        value_hex = chr(ord('A') + (value - 10))
        print(f"{value} menjadi {value_hex}")
        return value_hex
    else:
        raise ValueError("Digit tidak valid: harus antara 0 sampai 15.")