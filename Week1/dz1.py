# 1. Ввод и вывод данных
# Задача 2:
b = int(input())
h = int(input())
print(b*h/2)

# Задача 3:
n = int(input())
k = int(input())
print(k // n)
print(k % n)

# Задача 4:
n = int(input())
hour = n // 60
while hour > 23:
    hour -= 24
minute = n % 60
print(str(hour) + ':' + str(minute))

# Задача 6:
n = int(input())
print(f"The next number for the number {n} is {n + 1}.")
print(f"The previous number for the number {n} is {n - 1}.")

# 2. Условия
# Задача 2:
n = int(input())
if n > 0:
    print(1)
elif n < 0:
    print(-1)
else:
    print(0)

# Задача 3:
first1 = int(input())
first2 = int(input())
second1 = int(input())
second2 = int(input())
if (first1 + first2) % 2 == 0 and (second1 + second2) % 2 == 0:
    print('YES')
elif (first1 + first2) % 2 != 0 and (second1 + second2) % 2 != 0:
    print('YES')
else:
    print('NO')

# Задача 4:
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')

# Задача 6:
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# Задача 7:
first1 = int(input())
first2 = int(input())
second1 = int(input())
second2 = int(input())
if first1 == second1 or first2 == second2:
    print('YES')
else:
    print('NO')

# Задача 12:
n, m, k = int(input()), int(input()), int(input())
if n * m > k:
    if k < n * m and (k % n == 0 or k % m == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# 3. Вычисления
# Задача 1:
n = int(input())
print(n % 10)

# Задача 2:
v = int(input())
t = int(input())
if v > 0:
    s = v * t
    if s > 109:
        while s > 109:
            s -= 109
    print(s)
elif v < 0:
    s = abs(v * t)
    if s > 109:
        while s > 109:
            s -= 109
    print(109 - s)
else:
    print('Вася спит.')

# Задача 3:
n = float(input())
print(n - int(n))

# Задача 4:
n = float(input())
print(int((n - int(n)) * 100 // 10))

# Задача 5:
n = int(input())
lesson_time = 540 + (n * 45)
for i in range(2, n + 1):
    if i % 2 == 0:
        lesson_time += 5
    else:
        lesson_time += 15
print(str(lesson_time // 60) + ' ' + str(lesson_time % 60))

# Задача 6:
n, m = int(input()), int(input())
if m % n != 0:
    print(1 + int(m / n))
else:
    print(int(m / n))

# 4. Цикл for
# Задача 2:
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# Задача 4:
sum = 0
for i in range(10):
    sum += int(input())
print(sum)

# Задача 5:
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)

# Задача 6:
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)

# Задача 7:
n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)

# 5. Строки
# Задача 2:
str = input()
print(str.count(' ') + 1)

# Задача 4:
str = input()
n = str.find(' ')
print(str[n+1:] + ' ' + str[:n])

# Задача 5:
str = input()
if str.count('f') == 1:
    print(str.find('f'))
elif str.count('f') > 1:
    print(str.find('f'), str.rfind('f'), sep = ' ')

# Задача 6:
str = input()
if str.count('f') == 1:
    print(-1)
elif str.count('f') > 1:
    print(str[str.find('f') + 1:].find('f') + str.find('f') + 1)
else:
    print(-2)

# Задача 7:
str = input()
print(str[:str.find('h')] + str[str.rfind('h') + 1:])