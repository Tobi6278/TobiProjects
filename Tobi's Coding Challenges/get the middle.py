import math
def get_middle(s):
    length = (len(s) + 1) / 2
    if length.is_integer():
        return(s[int(length - 1)])
    else:
        return (f"{s[math.floor(length)- 1]}{s[math.ceil(length) - 1]}")
    
print(get_middle("test"))