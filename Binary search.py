from random import *
from math import *
mas = []

for _ in range(20): 
     x = randint(1, 100) 
     mas.append(x)
l, r = 0, 19
mas1=mas
mas1.sort()
print(mas1)
n = int(input('Уведіть кількість елементів масиву: '))
while abs(l-r)>1:
    m=ceil(len(mas1)//2)
    if n==mas1[m]:
        print("Число: " + str(n) + "\nID = "+str(m))
        break
    elif n > mas1[m]:
        l=m
    elif n < mas1[m]:
        r=m
        mas1=mas1[:r]
    else:
        print("Такого числа немає в списку")
        break
print(mas1[m])


        
    
        
