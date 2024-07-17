print('nhập vào độ dài 3 đoạn thẳng cách nhau 1 khoảng trắng')
a, b, c = map(float,input().split())

#if (a + b) > c > (a - b): #công thức này là hệ quả bất đẳng thức tam giác nên k chặc chẽ
if (a + b > c) and (a+c>b) and (b+c>a):
    print('{}, {}, {} là độ dài 3 cạnh của tam giác'.format(a,b,c))
else:
    print('{}, {}, {} không là độ dài 3 cạnh của tam giác'.format(a,b,c))