is_true = False
try:
    print('enter a and b, they are the range for value')
    a = int(input())
    b = int(input())
    is_true = True
except:
    print('input value is error')
if is_true:
  if a>b:
    print('a have to smaller than b')
  else:
    count = 0 #tạo cái biến đếm này để đặt giới hạn dừng, rằng mình chỉ lấy 10 giá trị tương ứng count = 10
    for i in range(a, b+1):
      if i%5==0:
        count += 1
        if count>10:
          print('\nmore than 10 values, pls cut off range')
          break
        print(i, end=' ')
    
    else:
      if count == 0:
       print('do not have any value %5==0')
      else:
       print('\nDone! That is all value device for 5 left 0')
