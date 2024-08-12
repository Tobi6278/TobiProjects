import math
def find_next_square(sq):
    sr = math.sqrt(sq)
    if (sr - math.floor(sr)) != 0:
     return -1
    else:
       return int(math.pow((sr + 1),2))

print(find_next_square(114))