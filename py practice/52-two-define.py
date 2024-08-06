def perfect_num_check(n):
    s = 0
    for i in range(1, (n//2)+1):
        if n % i == 0:
            s += i
    if n == s:
        return True
    return False

def per_list(n):
    for i in range(1, n):
        if perfect_num_check(i):
            print(i, end=' ')

try:
    n = int(input())
    if n < 0:
        print('n>0')
    else:
        per_list(n)

except:
    print('invalid')

