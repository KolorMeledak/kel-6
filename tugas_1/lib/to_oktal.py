def decimal_to_octal(number: int):
    if number == 0:
        return "0"
    
    octal = []

    while number > 0:
        octal.append(number % 8)
        number //= 8
        
    octal.reverse()
    return ''.join(map(str, octal))