def decimal_to_biner(number: int):
    if number == 0:
        return "0000"
    
    binary_number = []

    while number > 0:
        binary_number.append(number % 2)
        number //= 2

    binary_number.reverse()
    
    binary_number_to_string = ''.join(map(str, binary_number))
    
    return binary_number_to_string.zfill(4)