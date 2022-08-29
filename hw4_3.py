# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
import random
l = [random.randint (1, 17) for i in range (12)]
print(l)
l_unic = list(set(l))
print(l_unic)