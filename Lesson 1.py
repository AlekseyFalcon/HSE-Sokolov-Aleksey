# Создание переменных и вывод на экран
var1 = "Hello"
var2 = 42
var3 = True

print(var1)
print(var2)
print(var3)

# Ввод от пользователя и сохранение в переменные
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
string1 = input("Введите строку: ")

# Вывод на экран значений переменных
print("Первое число:", num1)
print("Второе число:", num2)
print("Строка:", string1)

# Проверка на тип и изменение объектов
print(type(var1), id(var1))
var1 = 123
print(type(var1), id(var1))

# Расчет времени
time_sec = int(input("Введите время в секундах: "))
hours = time_sec // 3600
minutes = (time_sec % 3600) // 60
seconds = time_sec % 60

print("Часы: ", hours)
print("Минуты: ", minutes)
print("Секунды: ", seconds)

# Запрос числа и расчет суммы
n = input("Введите число от 1 до 9: ")
if not n.isdigit():
    print("Неверный ввод!")
else:
    n1 = int(n)
    n2 = int(n*2)
    n3 = int(n*3)
    result = n1 + n2 + n3
    print("Сумма чисел n + nn + nnn:", result)