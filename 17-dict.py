#Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
#Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
#Các phần tử của Dict phải là một cặp key-value
#Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
#Các key buộc phải là một hash object

dic = {'name': 'Dyn', 'member': 69}
#print (dic)
#print (type(dic))

dic11 = {key : value for key, value in [('name','dyn'), ('member', 69)]}
#print (dic)
#print (type(dic))

dic15 = dict ()
#print (dic15)

iter_ = [('name', 'dyn'), ('mem', 69)]
dic19 = dict(iter_)
#print (dic19)
#print (type(dic19))

#Cứ hiểu đơn giản là giống như việc bạn khởi tạo biến và giá trị rồi đưa cho dict đó giữ giùm.
#Một lưu ý là những biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
name = 'bear'
dict23 = dict (name='dyn', ability= 'beauty', manifest= 'money')
#print (dict23) --> #{'name': 'dyn', 'ability': 'beauty', 'manifest': 'money'}

#iter29 = ('name', 'number', 69, False)
#dic_none = dict.fromkeys(iter29, 'money') #khoi tao dict, add value for keys
#print (dic_none)

iter29 = ('name', 'number', 69, False)
dic34 = dict.fromkeys(iter29, 'money')
#print (dic34[69])

dic34 ['name'] = 'beauty'
#print (dic34[69])

dic39 = dict(n='name', no=69, )
print (dic39)
dic39 ['n'] = dic39 ['n'] + 'gender'
dic39 ['no'] = dic39 ['no'] + 1

print (dic39)
print (dic39)
