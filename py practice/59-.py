def money(s):
    result = ''    
    for i in range(len(s)):
            if i % 2 != len(s) % 2:
                result += s[i]
    return result

s = input()
print(money(s))