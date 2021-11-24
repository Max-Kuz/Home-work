#1 Выводит тип данных елемента списка
list1 = [4,'laryngoscope', True, 'ETT #7.5', 60, 100.100, False]
for i in list1:
    print(type(i))

#2 вводим список вручную, меняем местами соседние елементы списка, последний оставляем нетронутым, если длинна списка нечетная
list2 = []
listLength = int(input("Введите размер списка"))
for i in range(listLength):
    list2.append(input("Введите елемент списка"))
print(list2)
for i in range (len(list2)-1):
    if i % 2 == 0:
        list2[i],list2[i+1] = list2[i+1], list2[i]
print(list2)

#3 Вводим номер месяца - нам возвращает пору года, в которой этот месяц. Замечу, что реализация через dict выглядит удобнее
month = int(input("Введите номер месяца от 1 до 12")) - 1
months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август', 'Сентябрь','Октябрь','Ноябрь','Декабрь']
if month in range(12):
    if month in range(2,5):
        print("{} - это весна".format(months[month]))
    elif month in range (5,8):
        print("{} - это лето".format((months[month])))
    elif month in range (8,11):
        print(("{} - это осень".format(months[month])))
    else:
        print("{} - это зима".format(months[month]))
else:print("Something went wrong")

fourSeasons = {1:"Зима",0:"Зима",11:"Зима",2:"Весна",3:"Весна",4:"Весна",5:"Лето",6:"Лето",7:"Лето",8:"Осень",9:"Осень",10:"Осень"}
print("Месяц под номером {} - {}".format(month+1, fourSeasons[month]))

#4 Вводим предложение, код разбивает его через пробелы на елементы и выводит первые 10 символов каждого с указанием номера
textTest = str(input("Введите текст"))
list4 = textTest.split(" ")
print(list4)
for i in range(len(list4)):
    print("Елемент {} -> {}".format(i+1,list4[i][:10]))

#5 Структура "рейтинг" - новый елемент занимает позицию по не возрастанию
numberArray = [5,4,4,3,2,1,1]
new = int(input("Введите новое число"))
numberArray.append(new)
for i in range(len(numberArray)-1,0,-1):
    if numberArray[i] > numberArray[i-1]:
        numberArray[i], numberArray[i - 1] = numberArray[i-1], numberArray[i]
print(numberArray)

#6 Список из кортежей, в которых есть номер и словарь с информацией о товарах. Задается пользователем через ввод.
# Потом выводится список уникальных значений каждого ключа ("аналитика")
listOfGoods = []
goods = []
x = [1, 1]
for i in range(2):
    goods.append({})
    goods[i]['Name'] = input("Введите название товара")
    goods[i]['Price'] = input("Введите цену товара ")
    goods[i]['Amount'] = input("Введите количество товара")
    goods[i]['Units'] = input("В чем измеряется кол-во товара?")
    x[0] = i + 1
    x[1] = goods[i]
    listOfGoods.append(tuple(x))
for i in range(len(listOfGoods)):
    print(listOfGoods[i])

Name = []
Price = []
Amount = []
Units = []
for i in range(2):
    Name.append(goods[i]['Name'])
    Price.append(goods[i]['Price'])
    Amount.append(goods[i]['Amount'])
    Units.append(goods[i]['Name'])

Name = list(set(Name))
Price = list(set(Price))
Amount = list(set(Amount))
Units = list(set(Units))
print('Name: ', Name)
print("Price: ", Price)
print("Amount: ", Amount)
print("Units: ", Units)