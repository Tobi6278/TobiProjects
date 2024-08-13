def magic_square():
    #List Making Block
    nums = input("Enter nine(9) numbers:").replace(" ","")
    sqaure = []
    lst = []
    ind = 0
    for i in nums:
        ind += 1
        lst.append(int(i))
        
        if ind >= 3:
            sqaure.append(lst)
            lst = []
            ind = 0
    
    #Checks if the sum of top,across and diagonal are equal
    return sum([sum(i) for i in sqaure])/3 == sum(sqaure[0]) and sum([i[0] for i in sqaure]) == sum([i[1] for i in sqaure]) == sum([i[2] for i in sqaure]) == sum(sqaure[0]) and sum([i[sqaure.index(i)] for i in sqaure]) == sum([i[-(sqaure.index(i) + 1) ] for i in sqaure]) == sum(sqaure[0])

print(magic_square())
        