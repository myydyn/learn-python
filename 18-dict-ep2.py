d = {'team':'work',(1,2):69}
#print(d)
#print(d.clear())
value = d.get('te', 'era')
#print(value)

d7 = {'team':'work',(1,2):69}
d8 = list(d7.items())
d9 = d7.keys()
d10 = d7.values()

d12 = {'team': 'Kteam',(1, 2): 69}
#print(d12)
#d14 = d12.pop((1, 2))
#print(d14) -> 69 #value
#print(d12) -> {'team': 'Kteam'} #con lai 

#d18 = d12.pop('acc', 'money') #pop a random key
#print(d18) -> 'money' # added default value to run not error

#d21 = d12.setdefault('money') #add a key and value default #None
#d22 = d12.setdefault('money', 'come to me')
#print(d12)
#print(d22)

d26 = d12.update(name= 'dyn') #update add more item, also can change the previous value of an existed key
#print(d12) -> {'team': 'Kteam',(1, 2): 69, 'name': 'dyn'}
