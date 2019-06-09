def print_formatted(number):    
    n = number
    size = len(bin(n)) - 2
    for i in range(1, n + 1):
        dec = str(i)
        octal = oct(i)
        hexadecimal = hex(i)
        binary = bin(i)
        print(dec.rjust(size), octal.lstrip("0o").rjust(size), 
              (hexadecimal.lstrip("0x").rjust(size)).upper(), binary.lstrip("0b").rjust(size))

