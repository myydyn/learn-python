#daph = [69, 68, 89]
#daph_update = []
#for m in daph:
#    daph_update.append(m + 1)
#print(daph_update)

#def inc(x): return x + 1 
#daph = [1, 2, 3]
#print(list(map(inc, daph)))

#print(list(map(lambda x: x +2, daph))) #map(lambda x: x >0, iterable) #lambda argument(s): expression

#func = lambda x, y: x + y
#m = [1, 2, 3, 4]
#n = [9, 8, 7, 6]

#lst = (map(func, m, n))
#print(list(lst))

#khai bao func
#func = lambda x: x > 0
#lst = [0, -1, -2, 1, 2, 3, 4]
#print(list(filter(func, lst)))

#khong khai bao func
#lst = [0, -1, -2, 1, 2, 3]
#print(list(filter(lambda x: x >0, lst)))

#dung 'if'
lst = [-5, 5, 4, -4, 6, 9, 0, -9]
#print([x for x in lst if x > 0])

#gửi None thay vì một function
    #kteam = [0, None, 1, 'Kteam', '', 'Free Education', 69, False]
    #list(filter(None, kteam))
#function là None, có nghĩa là Python sẽ sử dụng hàm bool mặc định để kiểm tra tính chân lý của từng phần tử trong kteam.
#Các giá trị Falsey trong Python bao gồm: 0, None, False, '' (chuỗi rỗng), và các đối tượng rỗng như [], {}, (), set(), v.v.
#Các giá trị trong kteam mà không phải là Falsey (tức là True) sẽ được giữ lại. Cụ thể:
    #0, None, '', và False đều là Falsey và bị loại bỏ.
    #Các giá trị còn lại: 1, 'Kteam', 'Free Education', và 69 đều là True, nên được giữ lại.
#khi print thi cho ket qua->[1, 'Kteam', 'Free Education', 69]

m_add = lambda x, y: x + y
m = [1, 2, 3, 4, 5]
from functools import reduce
#print(reduce(m_add, m))
print(reduce(m_add, m, 20))


