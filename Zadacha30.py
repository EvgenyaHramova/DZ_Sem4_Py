# Вычислить число  Пи c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math


d = input("Задайте значение точности числа π: ")
count = 0

if '.' in d:
    num = d.split('.')[1]
#print(num)    
for i in num:
    count+=1
#print(count)

print("π = ", round((math.pi), count))

