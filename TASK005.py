# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# В file1.txt :
# 2*x**2 + 4*x + 5

# В file2.txt:
# 4*x**2 + 1*x + 4

# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy
with open('file1.txt') as file1:
    eq1 = file1.readline()
with open('file2.txt') as file2:
    eq2 = file2.readline()

print(eq1)
print(eq2)

plus = str('+')

eqSum = sympy.simplify(eq1 + plus + eq2)

with open('result.txt', 'w') as file:
    file.write(str(eqSum))