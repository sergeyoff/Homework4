#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Задайте натуральное число: '))
sim_l = []
sim_num = 2
while num > 1:
    if num % sim_num == 0:
        sim_l.append(sim_num)
        num = num / sim_num
    else:
        sim_num += 1
print(sim_l)



