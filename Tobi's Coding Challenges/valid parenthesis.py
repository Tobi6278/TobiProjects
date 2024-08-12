def isValid(s):
    brackets = {"(":")","[":"]","{":"}"}
    keys = ["(","[","{"]
    values = [")","]","}"]
    ind = 0
    count = True
    for i in s:
      if s.count(keys[ind]) != s.count(values[ind]):
        count = False
        break
      ind += 1
      if ind > len(keys) - 1:
         break
      
      if brackets[s[0]] != s[-1]:
            if brackets[s[0]] != s[1] or s[-2] not in keys:
                count = False
                break 

           
    return count 



print(isValid("(){}{}"))