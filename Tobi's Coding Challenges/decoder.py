def decode(message):
    code = ""
    if len(message) % 3 == 0:

       l = [message[i:i+3] for i in range(0,len(message),3)]
       for i in l:
            code += i[-1] * int(i[0])
    return code
               
               



print(decode("2aB3fT5zR"))







