def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n-1)
try:
    n = int(input())
    if n < 0:
        print('n is a natural number')

    else:
        print(giai_thua(n))
except:
    print('invalid input')