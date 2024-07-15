
#write a program to display: 'Hi!', 'my', 'name', 'is', '{your nam}'.
#these word are seperated by '--' and your name is entered from keyboard

#cach 1: dùng hàm 'append' và 'join' (tự chế)
lst = ['Hi!', 'my', 'name', 'is']
print('Pls enter your name')
name = input()
lst.append (name)
print('--'.join(lst))

#cach 2: theo hướng dẫn, dùng hàm 'sep='
print('Pls enter your name')
name = input()
print('Hi!', 'my', 'name', 'is', name, sep='--')