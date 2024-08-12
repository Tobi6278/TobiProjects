
def narcissistic( value ):
    pow = len(str(value))
    num = 0
    for i in str(value):
        num += int(i) ** pow

    if num == value:
        return True
    else:
        return False
        
    
print(narcissistic(14607640612971980372614873089))