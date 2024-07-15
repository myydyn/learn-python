#def call_sum(lst):
#    print(lst)
#    if not lst:
#        return 0
#    else: 
#        return lst[0] + call_sum(lst[1:]) # cho lst[1:] la lay tu phan tu vi tri [1], bo qua cai dau tien la [0]
#print(call_sum([2, 3, 4, 5, 1]))

#def call_sum(lst):
 #   print(lst) # TIME: 11:01:24 PM
 #   return 0 if not lst else lst[0] + call_sum(lst[2:]) # return 0 if | not lst |  else: tra ve 0 | neu khong co lst (lst rong) | nguoc lai thi...

#print(call_sum([9, 1, 2, 3, 4, 8, 7, 6]))

#def call_sum(lst):
#    return lst[0] if len(lst) == 1 else lst[0] + call_sum(lst[1:])
#print(call_sum([1, 2, 3]))

def call_sum(lst):
    idx0, *r=lst
    return idx0 if not r else idx0 + call_sum(r) #paking
print(call_sum([1,2,3]))
print(call_sum(['a', 'b', 'c']))                                 
print(call_sum([[1, 2], [3, 4], [5, 6]]))
                                         
                                         
                                         
                                         
                                         
                                         
