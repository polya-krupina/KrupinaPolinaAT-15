digits = '0123456789ABCDEF'

def change_number_system(x, number_system):
    result = ''
    while x > 0:
        result = digits[x % number_system] + result
        x = x // number_system
    return result

a = float(input())
if int(a) != a:
    print('Неверный ввод')
else:
    a = int(a)
    print(change_number_system(a, 2) + ', ' + change_number_system(a, 8) + ', ' + change_number_system(a, 16))