def addTwoNumbers(l1, l2):
    new1 = []
    new2 = []
    sum1 = []
    for i in l1[::-1]:
        new1.append(f"{i}")
    for i in l2[::-1]:
        new2.append(f"{i}")
    sum = int("".join(new1)) + int("".join(new2))
    for i in str(sum):
        sum1.append(i)
    return sum1[::-1]
        
print(addTwoNumbers([2,4,3],[5,6,4]))