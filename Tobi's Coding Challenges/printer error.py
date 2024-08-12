def printer_error(s):
    range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    error = 0
    for i in s:
        if i not in range:
            error += 1
    return (f"{error}/{len(s)}")
    
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))