# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]


print('Натуральное число:')
n = int(input())
multiplierList = []
i = 2
while i * i <= n:
    while n % i == 0:
        multiplierList.append(i)
        n = n / i
    i = i + 1
if n > 1:
    multiplierList.append(n)
   
print('Простые множители: ', multiplierList)

uniqueElements = []
for i in range(len(multiplierList)):
    if int(multiplierList[i]) not in uniqueElements:
        uniqueElements.append(multiplierList[i])
print('Уникальные простые множители:', uniqueElements)


