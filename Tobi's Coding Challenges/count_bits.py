def count_bits(n):
    binary = []
    while True:
        div = n % 2
        binary.append(div)
        n = n // 2
        print(div)
        if n <= 0:
            break
   
    return binary.count(1)

num = int(input("Enter Number:"))
count = count_bits(num)
print(count)