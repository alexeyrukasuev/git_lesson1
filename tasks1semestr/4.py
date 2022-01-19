from random import randint
import random
 


x = int(input("rows:"))
y = int(input("columns:"))
mas = [-1, 1]
array = [[random.choice(mas) for j in range(y)] for i in range(x)]
print(str(array) + "\n")





