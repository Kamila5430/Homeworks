print('Введите количество n решений')
n = int(input())
sSum = 0.0
i = 1
while i <= n:
    s = 1.0/i
    sSum += s
    i = i+1
print('Общий путь:')
print(sSum)
sSum = 0.0
i = 1
while i <= n:
    if i % 2 == 0:
        s = 1.0/i
        sSum -= s
        i = i+1
    elif i % 2 != 0:
        s = 1.0/i
        sSum += s
        i = i+1
print('Расстояние от дома:')
print(sSum)
