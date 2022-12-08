# 3'. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

import random
randomList = []
for i in range(10):
    randomList.append(random.randint(-10, 10))
print(randomList)

uniqueElements = []
for i in range(len(randomList)):
    if int(randomList[i]) not in uniqueElements:
        uniqueElements.append(randomList[i])
print(uniqueElements)

