#def cal_rec_per(length, width):
    #per = (length + width)*2
#    per3 = length * width
    #return per
#    return per3

#rec_1_length = 5 #global
#rec_1_width = 3 #global
# khởi tạo một biến để hứng kết quả
#rec_1_per = cal_rec_per(rec_1_length, rec_1_width) #cho ham chay, tao bien hung gia tri

#print(rec_1_per)
# trường hợp này là khi bạn không cần tái sử dụng nó ở lần sau
#print(cal_rec_per(7, 4)) #positional argumment
#print(rec_1_length + rec_1_width)


#def satus():
#    print('How do you feel?')
#    # dòng dưới đây tương tự như bạn viết return None
#    return
#    print('can not display')

#none = satus()
#print(type(none)) 

#one, two, three = 'how', 'kteam', 69
#print(one)
#print(two)
#print(three)

#h, o, w = ('kteam', 69, 'daph')
#print(h, o, w)

def cal_rec_per(length, width):
    perimeter = (length + width)*2
    area = length * width
    return perimeter, area

rec_length = 10
rec_width = 4
rec_peri, rec_area = cal_rec_per(rec_length, rec_width)
print(rec_peri)
print(rec_area)

print(rec_length/rec_width)
