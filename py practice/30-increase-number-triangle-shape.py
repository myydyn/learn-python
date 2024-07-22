print('enter the value n')
it_is = False
try:
    n = int(input())
    it_is = True
except:
    print('value n is error')

if it_is:
    if 1<= n <9:
        count = 0
        for row in range(1, n+1):
            for column in range(1, row+1):
                print(column, end=' ')
            print()
    else:
        print('pls enter the value from 1 to 9')            

