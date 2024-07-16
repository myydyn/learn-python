# bài tự làm, dùng hàm round như excel nên k thể output các số 0 ở cuối nếu nhập m nhiều hơn phần thập phân của D
#print('nhap mot so thap phan D tu ban phim')
#D = float(input())
#print('nhap so chu so thap phan ban muon lam tron')
#m =int(input())
#print('so sau khi lam tron la:', round(D, m))


#làm theo hướng dẫn. dùng format
print('nhap mot so thap phan D tu ban phim')
D = float(input())
print('nhap so chu so thap phan ban muon lam tron')
m =int(input())
print('so sau khi lam tron la: ' '{0:.{1}f}'.format(D, m))