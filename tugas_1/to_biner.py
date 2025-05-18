def decimal_to_biner(number):
    if integer == 0:
        return "0000"
    
    binary_integer = []

    while integer > 0:
        binary_integer.append(integer % 2)
        integer //= 2

    binary_integer.reverse()
    
    binary_integer_string = ''.join(map(str, binary_integer))
    
    return binary_integer_string.zfill(4)