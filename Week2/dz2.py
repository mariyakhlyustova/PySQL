# 2. Условия:
# Задачa 8
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if abs(x - x1) <= 1 and abs(y - y1) <= 1:
    print('YES')
else:
    print('NO')

# Задача 9
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if abs(x - x1) == abs(y - y1):
    print('YES')
else:
    print('NO')

# Задача 10
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if abs(x - x1) == abs(y - y1) or x == x1 or y == y1:
    print('YES')
else:
    print('NO')

# Задача 13
n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n < m:
    N, M = n, m
else:
    N, M = m, n
if x <= N - x and x <= y and x <= M - y:
    print(x)
elif N - x <= y and N - x <= M - y:
    print(N - x)
elif y <= M - y:
    print(y)
else:
    print(M - y)

# 4. Цикл for
# Задача 9
n = int(input())
count = 0
for i in range(n):
    n = int(input())
    if n == 0:
        count += 1
print(count)

# Задача 11
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)

# 6. Цикл while
# Задача 2
n = int(input())
m = 2
while n % m != 0:
    m += 1
print(m)

# Задача 3
n = int(input())
count = 1
while 2 ** count <= n:
    count += 1
print(count - 1, 2 ** (count - 1))

# Задача 7
n = int(input())
sum = 0
count = 0
while n != 0:
    sum += n
    count += 1
    n = int(input())
print(sum / count)

# Задача 9
n = int(input())
max_n = 0
index = 0
index_max = 0
while n != 0:
    if n > max_n:
        max_n = n
        index_max = index
    index += 1
    n = int(input())
print(index_max)