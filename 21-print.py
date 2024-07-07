#print('Kteam', 'Free Education', 'one more argument')
#print(123, [1, 2, 3], 'Kteam')

#print('name', 'age', 2024, [123,2,3])

#print('Kteam', 'Python', 'Course') # sep mặc định là 1 khoảng trắng
#print('kteam', 69, 'free', sep=' :)) ')

#print('line 1', end=' ')
#print('line 2', end=' ')
#print('line 3', end=' ')

#from time import sleep # nhập hàm sleep từ thư viện time

#print('start....')
#sleep(3) # dừng chương trình 3 giây
#print('end...')

#from time import sleep
#print('start', end=' & ', flush=True)
#sleep(3)
#print('end')

#from time import sleep
#print('line1\n', 'line2', end='')
#sleep(3)
#print('end')

#with open('printtext.txt', 'w') as f:
 # print('printed by print function', file=f)
#with open('printtext.txt') as f:
 #f.read()

#with open('22-input-output-ep2.py', 'w') as f:
 # print('loading...', file=f)

from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()

from time import sleep

name = 'Daphne'
greeting = 'Hi! My name is Daphne. Enchanted to meet you!'

for c in greeting:
    print(c, end='', flush=True)
    sleep(0.1)
print()    