def decimal_to_biner(number):
    print("Perhitungan Desimal ke Biner")

    number = str(number)  # supaya aman buat split

    if number == "0" or number == "0.0":
        return "0000"

    integer, comma = number.split('.') if '.' in number else (number, '0')

    integer = int(integer)
    binary_integer = []

    while integer > 0:
        pembagian = integer // 2
        sisa = integer % 2

        print(f"{integer} \t dibagi 2 = {pembagian} sisa {sisa}")

        binary_integer.append(sisa)
        integer //= 2

    binary_integer.reverse()
    binary_integer_string = ''.join(map(str, binary_integer))
        
    comma = int(comma) / (10 ** len(comma))

    if comma == 0:
        return binary_integer_string

    binary_comma = []
    max_loop = 10

    print(f"\nKonversi bagian desimal ({comma}) ke biner:")
    for i in range(max_loop):
        if comma == 0:
            break

        comma *= 2

        bit = 1 if comma >= 1 else 0

        print(f"{comma:.3f}, bit yang terbentuk: {bit}")

        binary_comma.append(bit)

        comma = comma - 1 if comma >= 1 else comma

    binary_comma_string = ''.join(map(str, binary_comma))
    
    return binary_integer_string + '.' + binary_comma_string