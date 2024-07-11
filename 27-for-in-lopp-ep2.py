# k = list(range(3,9,2)) #list
# print(k)

# k = range(921)
# print(335 in k) #ham "in" print 'true/ false'

# lst = [5, (1,2,3), {'money', 'come to me'}]
# for i in range(len(lst)):
#   print(lst[i])

# lst = [1,2,3]
# for value in range(len(lst)):
#    lst[value] += 1
# print(lst)

# set_ = {5, 8, 1, 9, 4}
# sum_of_set = 0
# for value in set_:
#     sum_of_set += value
# print(sum_of_set)

# lst = ['$$'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('dapHne', 'Beauty', 'MONEY'), ('Come', 'To', 'Me')]]
# print(lst)

# lst = []
# for a, b, c in [('dapHne', 'Beauty', 'MONEY'), ('Come', 'To', 'Me')]:
#     a = a.capitalize()
#     b = b.upper()
#     c = c.lower()
#     lst.append(' $ $ '.join((a, b + c)))
# print(lst)

# lst = {key:value + 1 for key, value in (('Daphne', 69), ('Money', 79), ('Happy', 100)) if value % 2 != 0}
# print(lst)

# dict = {}
# for key, value in (('Daphne', 69), ('Money', 79), ('Happy', 100)):
#    if value % 2 != 0:
#        dict[key] = value + 1
# print(dict)

# manifest_list = ['money', 'diamond', 'ruby', 'jade']
# for manifest in manifest_list:
#   print(manifest)

# e = enumerate((manifest_list), 1)
# print(list(e))

# for index, manifest in enumerate(manifest_list, 1):
#   print(index, '-->', manifest )

# homework-1
#lst = []
#for a, b, c in [[1, 2, 3], [4, 5, 6]]:
 #   a = None
  #  lst.append((a, b, c))
#print(lst) >> [(None, 2, 3), (None, 5, 6)]


#lst60 = [[1, 2, 3], [4, 5, 6]]
#for l in lst60:
#    l[0] = None #trỏ vào từng phần tử cụ thể
#print(lst60) >> [[None, 2, 3], [None, 5, 6]]

# homework-2
n = int(input('Enter size of matrix: '))
dx, dy = 1,0
x, y = 0,0
spiral_matrix = [[None] * n for j in range(n)]

for i in range(n ** 2):
    spiral_matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and spiral_matrix[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy

for y in range(n):
    for x in range(n):
        print("%02i" % spiral_matrix[x][y], end=' ')
    print()

print()
