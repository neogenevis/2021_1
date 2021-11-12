# Task 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

name = 'Valeria'
age = 25
period = int(input("How long will you study this programm?"))
age_period = age + period
print('Hey, my name is', name, 'and I am', age)
print('After  ending this course I will be', age_period)

# Task 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# Task 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.

n = int(input('Введите число - '))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print('Сумма чисел n + nn + nnn - %d' % total)

# Task 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input('Введите целое положительное число ')))
max = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

# Task 5 Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

profit = int(input('Enter revenue values '))
costs = int(input('Enter cost values '))

if profit > costs:
    print(f'Congrats, your profitability is {profit / costs:.1f}')
    workers = int(input('How many workers do you have? '))
    print(f'One worker make {profit / workers: .1f}')
else:
    print('You operating at a loss, provide a fundamental analysis')

# Task 6 Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать
# значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Enter your results after the first running (in km)'))
b = int(input('Enter your expected goals (in km)'))
days = 1
km = a
if a <= 0 or b < 0:
    print('Your goal have to be greater than zero')
while km < b:
    a += a * 0.1
    days += 1
    km = km + a
    print(f'U will get the point in {days} days')
    break


# Task 1
number = int(input('Pick a number, please: '))
print(number + 2)

# Task 2
num = int(input("Введите число: "))
while True:
    if 0 < num < 10:
        print(num ** 2)
        break
    else:
        num = int(input("Введите число от 0 до 10: "))
        print('Error')

# Task 3
name = input('Add your name')
surname = input('Add your surname')
age = int(input('Add your age'))
weight = int(input('Add your weight?'))

if age <= 30 and weight > 30 or weight < 120:
    print(name, surname, ', Вы в хорошем состоянии')

if age >= 30 and weight < 50 or weight > 120:
    print(name, surname, ', Вам требуется заняться собой')

if age >= 40:
    if weight < 50 or weight > 120:
        print(name, surname, ', Вам требуется врачебный осмотр')

else:
    print('Take care of yourself!')
    print('end')