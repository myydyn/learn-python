#def eve(a, b, c):
#    return (a+b+c)/2
#e = eve(1, 2, 3)
#print(e)

#evil = lambda e, f, g: (e+f+g)/3
#print(evil(3,2,1))

#def power(x, a = 2):
#    return (x ** a)
#m = power(2)
#print(power(2))
#n = power(2, 3)
#print(n)

#angle = lambda x, a = 2: x**a
#print(angle(2, 3))

#print(a**5) #phan biet local va globa
# 
#def young():
#    mem = lambda x: x + ' belong to daph'
#    return mem

#lady = young()
#print(lady('beauty'))
#print(lady)

#timeless = [lambda x: x**2, lambda  x: x**3, lambda x: x**4]
#print(timeless[2](3)) #[vi tri phan tu] (gia tri phan tu do)

#for m in timeless:
#    print(m(3))


#greater = lambda x, y: x if x > y else y
#print(greater(23, 69))

#charming = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
#print(charming(21))

#def best(first_str):
#    return lambda second_str: first_str + second_str
#call = best('money')
#print(call)
#print(call(' come to me'))

daph = lambda goal: (lambda money: goal + money)
slogan = daph('baeuty')
slogan('cutie')
print()
print(lambda goal: (lambda money: goal + money))