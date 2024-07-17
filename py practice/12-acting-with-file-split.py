with open('bai1.12.inp', 'r') as inp_file:
    lst = inp_file.read().splitlines()
    str = ' '.join(lst)

with open('bai1.12.out', 'w') as out_file:
    out_file.write(str)

