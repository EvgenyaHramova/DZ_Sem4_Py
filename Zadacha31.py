# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Задайте число: "))
list = []
i = 2
while i <= num:
    if num % i == 0: # and (1 < i < num)
        list.append(i)
        num = num / i  #num//=i
    i +=1

print(list)
