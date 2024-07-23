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
            print() #dòng này để vòng lặp in hết 1 dòng là xuống hàng
    else:
        print('pls enter the value from 1 to 9')            

## 2ND CODE
while True:
    try: 
        n = int(input('Nhập số nguyên n từ 1 đến 9: '))
        ketqua = ''
        if 0 < n < 10:
            break
        else:
            print('n là số nguyên từ 1 đến 9, nhập lại...')
    except:
        print('Nhập sai dữ liệu đầu vào, nhập lại...')
for i in range(1,n+1):
    # ban đầu kết quả là 1, sau mỗi vòng lặp sẽ cộng vào 1 số i
    ketqua -= '{} '.format(i)
    # in kết quả ra, mỗi lần in xong xuống dòng
    print(ketqua, end = '\n')
