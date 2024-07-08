#five_even_numbers = []
#k_number = 1

#while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    #if k_number % 2 == 0: # nếu k_number là một số chẵn
    #    five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
   # if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
  #      break # thì kết thúc vòng lặp
 #   k_number += 1

#five_even_numbers
#[2, 4, 6, 8, 10]#
#k_number
#10

#three_even_numbers = []
#k_no = 1
#while True:
    #if k_no % 5 == 0:
    #    three_even_numbers.append(k_no)
   # if len(three_even_numbers) == 3:
  #      break
 #   k_no +=2

#print('3 no. is', three_even_numbers)
#print(k_no)

#lst = []
#k_number = 1
#while k_number < 10:
 #    if k_number % 2 == 0: # nếu k_number là số le
  #      lst.append(k_number)
   #     break
    #    #k_number += 1  # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
     #   #continue
#print(lst)
#k_number += 1

k_number = 1
while k_number < 10:
     if k_number % 2 != 0: # nếu k_number là số chẵn
         k_number += 1  # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
         continue
     print(k_number, 'is odd number')
     k_number += 1

open('25-.py', 'w')