# Viết hàm trả về hai danh sách sau khi đã hoán đổi nữa sau danh sách cho nhau. 
# (Tham số là 2 danh sách bất kỳ).
# vd: 1 2 3 4 5 6  7                 || output: 1 2 3 three four five
#     one two three four five        ||         one two 4 5 6  7

def cheo(m, n):
    nuaDong1 = len(m) // 2
    nuaDong2 = len(n) // 2

#Su dung ky thuat Indexing va Cat list de thuc hien yeu cau de bai
    nuaDong1Moi = m[nuaDong1:]
    nuaDong2Moi = n[nuaDong2:]
    
    dong1Moi = m[0:nuaDong1] + nuaDong2Moi
    dong2Moi = n[0:nuaDong2] + nuaDong1Moi

    return dong1Moi, dong2Moi

m = input('nhap dong 1: ').split()
n = input('nhap dong 2: ').split()

dong1, dong2 = cheo(m, n)
print(*dong1)
print(*dong2)


# nhức nhức cái đầu quá, cắt ra 4 đoạn nhỏ, với dòng đầu là đoạn 1 và 2, 
# dòng sau là đoạn 3 và 4 rồi 'ghép' lại bằng cách '+', sao cho đoạn 1 + 4
# thành dòng thứ 1 mới. đoạn 3 + 2 thành dòng 2 mới