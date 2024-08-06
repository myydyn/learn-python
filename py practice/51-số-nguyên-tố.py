import math
def  kiemTrasoNguyenTo(n):
    if n == 1:  #last -2 and more below
        return False
        
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def lst_so_ngto(a, b):
    for i in range (a, b+1):
        if kiemTrasoNguyenTo(i):  #last -1
            print(i, end=' ') #last step

try:
    a = int(input())
    b = int(input())
    if a<0 or b<0:
        print('a and b iz greater than 0')
    elif a>b:
        print('a is smaller than b')
    else:
        lst_so_ngto(a, b)
except:
    print('invalid input')
