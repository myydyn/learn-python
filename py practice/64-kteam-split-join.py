def deux(s):
    cheTuBoDauCach = s.split() # gặp space là cắt thành các unit nhỏ
    result = '-'.join(cheTuBoDauCach) # chen giữa các unit bằng join
    return result

s = input()
print(deux(s))