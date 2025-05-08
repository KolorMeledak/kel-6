def decimal_to_biner(number):
    integer, comma = number.split('.') if '.' in number else (number, '0')

    integer = int(integer)
    binary_integer = []

    while integer > 0:
        binary_integer.append(integer % 2)
        integer //= 2

    comma = int(comma) / (10 ** len(comma))

    binary_comma = []
    max_loop = 10

    while comma > 0 and len(binary_comma) < max_loop:
        comma *= 2
        binary_comma.append(1 if comma >= 1 else 0)
        comma = (comma - 1) if comma >= 1 else comma

    binary_integer.reverse()
    
    binary_integer_string = ''.join(map(str, binary_integer))
    binary_comma_string = ''.join(map(str, binary_comma))
    
    if binary_comma_string == '':
        return binary_integer_string
    else:
        return binary_integer_string + '.' + binary_comma_string

            