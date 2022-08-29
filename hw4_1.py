# Вычислить число c заданной точностью d
import random
from decimal import getcontext, Decimal

d = int(input('Введите заданную точность округления числом: '))
num_1 = int(random.randint(1, 50))
num_2 = int(random.randint(1, 100))
getcontext().prec = d
print(Decimal(num_1) / num_2)
