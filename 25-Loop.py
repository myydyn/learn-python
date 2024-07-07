#open('26-.py', 'w')

#k = 5
#while k > 0:
 #    print('k =', k)
  #   k -= 1


#s = 'How Kteam'
##idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
#length = len(s) # lấy độ dài chuỗi làm mốc kết thúc
#while idx < length:
 #    print(idx, 'stands for', s[idx])
  #   idx += 1 # di chuyển index tới vị trí tiếp theo


#five_even_numbers = []
#k_number = 0

#while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
     #if k_number % 2 == 0: # nếu k_number là một số chẵn
    #     five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
   #  if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
  #       break # thì kết thúc vòng lặp
 #    k_number += 1

#print(five_even_numbers)
#print(k_number)

k_number = 1
while k_number < 10:
     if k_number % 2 == 0: # nếu k_number là số chẵn
         k_number += 1  # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
         continue
     print(k_number, 'is odd number')
     k_number += 1

