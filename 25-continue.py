lst2 = []
lst5 = []
k_no = 1
while k_no < 50:
    if k_no % 5 == 0:
        lst5.append(k_no)
        k_no += 1
        continue    
    if k_no %2 == 0:
        lst2.append(k_no)
    k_no += 1

print(lst5)
print(lst2)
open('25-while-ele.py', 'w')