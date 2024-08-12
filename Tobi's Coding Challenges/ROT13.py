def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    new_list = []
    for i in message:
        if i.isalpha():
            index = alphabet.index(i.lower()) + 13
            if index > 25:
                index = index - 26
            if i.isupper():
                new_list.append(alphabet[index].upper())
            else:
                new_list.append(alphabet[index])
            index = 0
        else:
            new_list.append(i)
    return "".join(new_list)
        
print(rot13("Hello how are you"))