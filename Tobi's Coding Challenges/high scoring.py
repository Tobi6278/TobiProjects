def high(x):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    score = 0
    store = []
    for i in x.split():
        for j in i:
            score += (alpha.index(j) + 1)
        store.append(score)
        score = 0
    return x.split()[store.index(max(store))]

print(high("man i need a taxi up to ubud"))
