#{1,2} #k chứa trùng lặp  #

set_1 = {69,96}

set_2 = {'salut'}
#print (set_2)
#3print (type(set_1))
#k chứa được unhashable nhưng chính nó là unhashable #weir

set_3  = {'money', 68, 'move'}
#print (set_3) #{68, 'move', 'money'}

set_4 = {}
#print (type(set_4)) #k the tao empty set

set5 = {value for value in range (4,9)}
#print (set5)
#print (type(set5))

set20 = set((1,5,7,6,2,8,3,4))#contructor
#print (set20)
#print (type(set20))

set24 = set('money')
##print (set24) #{'m', 'n', 'y', 'e', 'o'}  #k quan tam vi tri cac phan tu
#print (type(set24))

set28 = set ('aaaaaaaa,a,a')
#print (set28)

set31 = set ([1,23,2,1,3,4,7,5,8,5,3,6])
#print (set31)

set34 = set()
#print (set34) 

s37 = (1 in {1,3,4})
#print (2 in {1,3,4})

s40 = ({1,3,4} - {4,3})
#print (s40)

#print ({1,5,4,3} ^ {3,9,4}) ###phep so sanh

seta = {1,3,4,5}
setb = {9,3,4}

setc = seta & setb
setd = seta | setb

set51 = setd  - setc

#print (setc)
#print (setd)
#set51.pop () #lay ra phan tu dau tien trong day, k co gia tri trong ()
#set51.remove (5) #xoa phan tu 5, chi 1 phan tu, phai co gia tri trong ()
#set51.discard (9) #loai bo phan tu (9), hien ra cac phan tu con lai
#print (set51.copy ()) #sao chep
#set51.add(2,3) #set.add() takes exactly one argument (2 given)

set61 = {9,2,1}
print (id(set61))
set61.add (4)
print (set61)
print (id (set61))

