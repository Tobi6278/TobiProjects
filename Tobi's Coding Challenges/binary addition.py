def add_binary(a,b):
    binary = list(bin(a + b))
    return "".join(binary[2::])

print(add_binary(1230,4))