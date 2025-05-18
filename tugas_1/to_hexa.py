def decimal_to_hexa(number):
    integer = int(number)
    hexa = []

    while integer > 0:
        hexa.append(integer % 16)
        integer //= 16
        
    hexa.reverse()
    return ''.join(map(str, hexa))