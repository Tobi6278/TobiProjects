def no_rep(s:str) -> str:
    words = []
    lst = []
    for i in s:
        if i in lst:
            words.append("".join(lst))
            lst = []
            lst.append(i)
        else:
            lst.append(i)
    words.append("".join(lst))
    return  [i for i  in words if len(i) == max([len(i) for i in words])][0]
print(no_rep("a"))