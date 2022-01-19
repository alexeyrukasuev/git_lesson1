from random import randint
x = int(input())
y = int(input())
mas = [[randint(0, 100 + 1) for j in range(y)] for i in range(x)]
print(mas)
