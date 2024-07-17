with open("bai2.12.inp",mode="r") as f:
    noidung=f.read().replace("\n"," ") # dùng replace thay split

with open("bai2.12.out",mode="w") as a:
    a.write(noidung)