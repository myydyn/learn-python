def bieu_thuc(so1, phep_tinh, so2):
    if phep_tinh == ':':
        if so2 == 0:
            return 'so chia phai khac 0, hay nhap lai'
        else:
            ket_qua = so1 / so2
    elif phep_tinh == '+':
        ket_qua = so1 + so2
    elif phep_tinh == '-':
        ket_qua = so1 - so2
    elif phep_tinh == '*':
        ket_qua = so1 * so2
    else:
        return 'invalid'
    return '{} {} {} = {}'.format(so1, phep_tinh, so2, ket_qua)

try:
    so1, phep_tinh, so2 = input().split()
    so1 = float(so1)
    so2 = float(so2)

    result = bieu_thuc(so1, phep_tinh, so2)
    print(result)

except:
    print('invalid input')