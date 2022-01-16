#1) Создать переменную типа String
a ='a'
print(type(a), 'A =', a)
#2)Создать переменную типа Integer
b = 21
print(type(b), 'B =', b)
#3) Создать переменную типа Float
c = 21.17
print(type(c), 'C =', c)
#4) Создать переменную типа Bytes
e = bytes(14)
print(type(e), 'E =', e)
#5) Создать переменную типа List
l = list [2, 7, 'wow']
print(type(l), 'L =', l)
#6) Создать переменную типа Tuple
t = (2, 7, 'wow')
print(type(t), 'T =', t)
#7) Создать переменную типа Set
s = {2, 7, 'wow'}
print(type(s), 'S =', s)
#8. Создать переменную типа Frozen set
fs = {2, 7, 'wow'}
fs = frozenset(fs)
print(type(fs), 'FS =', fs)
#9) Создать переменную типа Dict
dc = { 'al': 'Alex',
       'vd': 'Vadim' }
print(type(dc), 'DC =', dc)

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# done))
#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
ma = 'mama +'
pa = ' dad'
ya = (ma+pa)
print (type(ya), 'Ya = ', ya)
#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
now = 'sunday'
day = 16
nowday = (now + ','+ str(day))
print (type(nowday), nowday)
#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
i= 'alex'
o = 22
old= (i + '+'+ str(o))
print (type(old), old)
