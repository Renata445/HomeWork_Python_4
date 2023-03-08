n = int(input('Введите кол-во кустов: '))
a = list()
for i in range(n):
    x = int(input('Введите кол-во ягод в каждом кусте: '))
    a.append(x)
b = list()
for i in range(len(a) - 1):
    b.append(a[i - 1] + a[i] + a[i + 1])
b.append(a[-2] + a[-1] + a[0])
print(max(b))