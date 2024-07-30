def intro(name, age):
    print('Hi! My name is {}. I am {}-year-old.'.format(name, age))
#dùng hàm để tái sử dụng phần phía trên này
try:
    name = input('your name is ')
    age = int(input('your age is '))

    if age<1:
        print('age is positive, pls')
    else:
        intro(name, age)
except:
    print('error')