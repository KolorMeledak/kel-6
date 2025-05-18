def decimal_to_hexa(number: int):
    if number == 0:
        return "0"
    
    hexa = []

    while number > 0:
        hexa.append(number % 16)
        number //= 16
        
    hexa.reverse()
    return ''.join(map(str, hexa))