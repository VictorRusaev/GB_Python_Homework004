# 1'. Вычислить число Пи c заданной точностью d
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415 

import math
d = input('Точность: ')
length = len(d)
p = str(math.pi)
for i in range(length):
    print(f'{p[i]}', end = '')
