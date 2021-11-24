#1 создать переменные и вывести на экран
a = 10
print(a)
b = input("Введите число")
print(b)
#2 вводится время с секундах - вывод время в формате чч:мм:сс
time = int(input("Введите время в секундах"))
hh = time //3600
mm = (time % 3600) //60
ss = time %60
print("{}:{}:{}".format(hh,mm,ss))
#3 Ввод числа - вывод n+nn+nnn
num = input("Введите число")
array = []
for i in range(3):
    array.append(str(num)*(i+1))
print(array)
print (int(array[0])+int(array[1])+int(array[2]))
#4 Найти найбольшую цифру в числе
num = input("Введите многоциферное число")
max = 0
i = 0
while i<len(num):
    if int(num[i]) > int(max):
        max = num[i]
    i=i+1
print(max)
#5 Вводим выручку и затраты. Получаем вердикт и рентабельность, если работаем в плюс
inc = int(input("Введите выручку фирмы"))
exp = int(input("Введите издержки фирмы"))
profit = inc - exp
if inc > exp:
    print("Фирма работает с прибылью {} , рентабельность выручки при этом {:04.2f}%".format(exp,(profit*100)/inc))
elif inc == exp:
    print("Фирма выходит в ноль")
else:
    print("Работаем в минус")
#6 Шпортсман бежит на 10% больше с каждым днем. Вводим сколько бегает в день 1, сколько хотим бегать - получаем день, когда это случится
baseline = int(input("Сколько спортсмен пробегает сейчас?"))
result = int(input("Сколько спортсмену нужн пробегать?"))
day = 1
while baseline < result:
    day = day + 1
    baseline = baseline*1.1
print("На {} день спортсмен сможет пробежать {:0.1f} км".format(day,baseline))
#Test of commit and push
