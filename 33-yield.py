#daph = [68, 'beauty', 69]
#for x in daph:
#    print(x)

#daphne = (value for value in range(4))
#for value in daphne:
#    print(value)
    

#def square(lst):
#    sq_lst = []
#    for num in lst:
#            sq_lst.append(num**2)
#    return sq_lst

#get_fr = square([1, 2, 3, 4])
#for value in get_fr:
#    print(value)    

#def gfr(lst):
#    bfr = []
#    for num in lst:
#            bfr.append(num**2)
#    return bfr
#    #yield bfr

#get_info = gfr([2, 4, 6])
#for value in get_info:
#    print(value)


#def daph(lst):
#     for num in lst:
#            yield num**2

#salmon = daph([6, 9])
#for value in salmon:
#      print(value)

#def gen():
#    for value in range(3):
#            print('yield', value + 1)
#            yield value

#for val in gen():
#      print(val)

#SEND
def gen():
    for i in range(2, 6):
        x = yield i
        print('loading', x)
g = gen()
next(g)
g.send('beauty')
next(g)
g.send(69)


