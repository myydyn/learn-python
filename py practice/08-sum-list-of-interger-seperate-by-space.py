print('nhap chuoi cac so nguyen, cach nhau khoang trang')
# chỗ này phải nhập các số nguyên cách nhau 1 khoảng trắng để input đầu vào là kiểu chuỗi, mỗi số là 1 phần tử trong chuỗi
daysonguyen = input()
chuoiduoctach = daysonguyen.split() # split để tách từng phần tử của chuỗi trên
epkieu = map(int, chuoiduoctach) # ép kiểu sau khi các phần tử độc lập, chỉ các phần tử là số nguyên mới phù hợp, nếu k thì báo lỗi

tinhtong = sum(epkieu)
print(tinhtong)


#join: k dùng được
