def longestCommonPrefix(strs):
    prefex = []
    lengths = [len(i) for i in strs]
    index = 0
    index1 = 0
    count = 0
    while True:
        if index1 <= min(lengths) - 1:
            if strs[index][index1] == strs[0][index1]:
                count += 1
                index += 1
            else:
                break
            if index >= len(strs):
                if count == len(strs):
                    prefex.append(strs[0][index1])
                    count = 0
                    
                index = 0
                index1 += 1    
        else:
            break   
    return "".join(prefex)


print(longestCommonPrefix(["aa","aa","aa"]))

        

        