try:
    name = input('enter your name ')
    age = int(input('enter your age '))
    
    if age<1:
        print('your age has to a positive number')
    else:
        print('Hi! My name is {}, I am {}-year-old'.format(name, age))
except:
    print('invalid input')
