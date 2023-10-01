a = float(input())
if int(a) != a:
    print('Неверный ввод')
else:
    a = int(a)
    print(str(bin(a))[2:]+', '+str(oct(a))[2:]+', '+str(hex(a))[2:])