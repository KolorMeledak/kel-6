def decimal_to_octal(number):
    octal = []

    while integer > 0:
        octal.append(integer % 8)
        integer //= 8
        
    octal.reverse()
    return ''.join(map(str, octal))