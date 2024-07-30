def ssum(*args):
    print(*args,sep=' + ',end=f' = {sum(args)}\n')

# test function
ssum(9,99,999,9999)

#*args trong định nghĩa hàm ssum cho phép hàm nhận một số lượng không xác định các đối số.