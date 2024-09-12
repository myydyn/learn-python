# Trả về set các phần tử riêng và set các phần tử chung của hai set.
# (Với tham số là hai set bất kỳ)
# in:  Kteam Free Chao Education
#      Education Nam Moi Free 2021 
# out: {'Chao', 'Nam', 'Moi', 'Kteam', '2021'}
#      {'Free', 'Education'}

def chungRieng(x, y):
    # Phép toán  x ^ y: là phép toán XOR trên các tập hợp, 
    # trả về các phần tử thuộc tập hợp x hoặc y nhưng không thuộc cả hai (các phần tử "riêng lẻ").
    rieng = x ^ y
    # x & y: phép toán AND trên các tập hợp, tức là nó trả về các phần tử chung giữa x và y.
    chung = x & y
    return rieng, chung   

x = set(input('nhap set 1: ').split())
y = set(input('nhap set 2: ').split())

rieng, chung = chungRieng(x, y)

print(rieng)
print(chung)
