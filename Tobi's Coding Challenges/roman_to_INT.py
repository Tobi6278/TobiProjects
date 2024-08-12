def romanToInt(s):
    w = [i for i in s]
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    num = 0
    for i in w:
        if w.index(i) + 1  > len(w) - 1:
            num += roman[s[-1:]]
            break
        elif i == "O":
            num += 0
        elif roman[i] < roman[w[(w.index(i)) + 1]]:
            num += (roman[w[(w.index(i)) + 1]] - roman[i])
            w[w.index(i) + 1]= "O"
        
        else:
            num += roman[i]
        w[w.index(i)] = "O"
        
    return num

print(romanToInt("III"))
                

           

