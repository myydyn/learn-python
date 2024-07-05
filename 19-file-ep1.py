#a = open('19-test.txt')
#b = a.read(5) -> #in ra 'How K' (5) la so ky tu in ra
#b = a.read() -> #in ra full neu bo  trong ()
#b = a.read()
#c = a.read()
#print(b)
#print(c)

#f9 = open('19-test.txt')
#f10 = f9.read()
#f9.close()

#f9 = open('19-test.txt')
#f18 = f9.read()

#print(f10)
#print(f18)

#f9.read(10)
#print(f9)

#f9.read() # con trỏ file ở vị trí cuối cùng, bạn không thể đọc được gì nữa

#f9.close() # nhớ đóng file

#fobj = open('19-test.txt')
#f27 = fobj.readline()
#f28 = fobj.readline()
#print(f27) 
#print(f28)
#How Kteam
#Free Education

#fobj = open('19-test.txt')
#f27 = fobj.readlines()
#print(f27) #['How Kteam\n', 'Free Education\n', '\n', 'Share to better\n', '\n', "print('hello world!')\n"]

#fobj = open('19-test.txt', mode='r')
#f39 = fobj.write('The first line\n') # thêm \n để kết thúc 1 dòng

#f39 = fobj.write('And last line too')

#fobj.close()
#print(f39)

fobj = open('19-test.txt', mode='r')
f47 = fobj.read()
#"How Kteam\nFree Education\n\nShare to better\n\nprint('hello world!')\n"
fobj.seek(0)
f50 = fobj.read()
fobj.close()
print(f47)
print(f50)

