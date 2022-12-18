n =input('Введите вещественное число - ')
a = n
n = n.replace('.', '')
n = n.replace('-', '')
n4 = int(0)
for i in n:
    n4 = n4 + int(i)
print(f'Сумма всех цифр в числе {a} равна {n4}')

import decimal
from decimal import Decimal
# import decimal
# decimal.getcontext().prec = 2
q = int(input('задайте количетво элементов в списке - '))
# sum = decimal(num)
sum = int(0)
q_list = []
for i in range(1, (q + 1)):
    i = ((1 + (1/i))**i)
    sum = sum + i
    q_list.append(i)
print('Получившиеся элементы ')
print(*q_list)
print(f'Сумма всех элементов равна {sum}')

import time
ll = int(input('Введите количетво элементов в списке - '))
print('Введите элементы списка:')
l = []

for i in range(ll):
    li = input()
    l.append(li)

a = list()
n = list()

for i in range(0, len(l)):
    b1 = time.time()
    b1 = str(b1)
    b1 = b1.replace('.', '')

    b1 = b1[-4:]
    b1 = int(b1)
    a.append(b1)
    time.sleep(0.1)

    t_emp = list()
    t_emp.append(b1)
    o = i

    t_emp.append(l[o])
    n.append(t_emp)
    n.sort()

print('Перемешанный список:')
for i in range(len(n)):
    print(n[i][1])