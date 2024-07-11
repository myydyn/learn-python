#def kteam(k, t, e, r):
#    print(k),
#    print(t, e),
#    print(r)
#kteam(123, 'daph', 69.96, 'beauty')
#lst = [123, 'daph', 69.96, 'beauty']
#kteam(lst[0], lst[1], lst[2], lst[3])
#kteam(*lst)

#def timeout(*, b = 'bella', c = 'cindy'):
#    print(b, c)

#lst = ('bee', 'cindy')
#timeout()    

#def daph(*args, dyy):
#    print(args)
#    print(dyy)
#daph('to late', 68.69, 'try more')
#daph(*(x for x in range(7)), dyy = 68)
#daph(69, 70)

#dic = {'name':'Daphne', 'number':69}
#def Daph(name, number):
#    print('name ->', name)
#    print('number ->', number)   
#Daph(**dic)

#def kteam(**kwargs):
#    print(kwargs)
#    print(type(kwargs))
#kteam(name='daph', number=69)#packing from tuple to dict

def kteam(**kwargs):
    for key, value in kwargs.items():
        print(key, '->', value)
kteam(id=3424, name='Henry', age=18, lang='Python')

