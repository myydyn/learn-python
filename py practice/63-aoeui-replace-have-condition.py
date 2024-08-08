def str(s):
    nguyen_am = 'aoeuiAOEUI'
    tongNgAm = 0
    for c in nguyen_am:
        tongNgAm += s.count(c)
        s = s.replace(c, '$')
    return tongNgAm, s
s = input()

soLuong, ketQua = str(s)

print(soLuong)
print(ketQua)
