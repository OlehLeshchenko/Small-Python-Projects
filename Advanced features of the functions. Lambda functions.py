# -*- coding: utf-8 -*-
"""Лещенко Олег - Функції.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q5VbPPnNh42pc8NmOWWzD7mOverDjiUF

**Необов'язкові параметри**

Під час виклику до функції можна передавати менше параметрів, ніж формальних параметрів у її заголовку. Необов'язкові параметри можуть мати значення за замовчуванням. Їх записують після обов'язкових параметрів.
"""

def dlina(x1, y1, x2=0, y2=0):
   l = ((x2-x1)**2 + (y2-y1)**2)**0.5
   return l
s = dlina(3, 4)
print(s)

"""**Передавання параметрів у іншому порядку**

Під час виклику параметри до функції можна передавати в зміненому порядку, указавши імена та значення параметрів.
"""

s = dlina(0, x2=3, y1=0, y2=4)
print(s)

"""**Довільна кількість аргументів** 

Якщо перед іменем формального параметра у заголовку функції поставлено символ *, то аргументом цієї функції може бути будь-який набір даних.
"""

def suma(*x):
   s = 0
   for i in x:
      s += i
   return s
print(suma(1, 3, 5))
print(suma(2, 4, 6, 8, 1))

"""**Анонімні функції (лямбда-функції)**

Загальний вигляд:

*lambda аргументи: вираз*

* Вираз - повертає лише одне значення або не повертає жодного. 
* Вираз записаний в один рядок, не містить циклів і розгалужень. 
* Аргументи перераховані через кому. Можуть бути відсутні. 
Можуть мати значення за замовчуванням.
"""

f = lambda x: x**3
a = int(input("a = "))
print("Об'єм куба", f(a))

"""Опрацювання списків з використанням функції map"""

sp = [1, 2, 3, 4]
kv = list(map(lambda x: x**2, sp))
print(kv)

"""Опрацювання списків з використанням функції filter


"""

sp = [1, 2, 3, 4]
kv = list(filter(lambda x: x%2==0, sp))
print(kv)

"""**Задача 1.** 

Уведіть координати точки та радіус кола. Визначте, чи міститься точка усередині кола з заданим радіусом і центром у початку координат, виведіть "Так" або "Ні". Для отримання відповіді використайте лямбда-функцію.

"""

f = lambda x,y,r,a=0,b=0: 'Так' if (x-a)**2+(y-b)**2<=r**2 else 'Ні'
x=float(input("Уведіть x= "))
y=float(input("Уведіть y= "))
r=float(input("Уведіть радіус кола: "))  
print(f(x,y,r))

"""**Задача 2.** 

Уведіть список цілих чисел та окреме число. Відніміть від кожного елемента списку отримане число. Виведіть змінений список. Для опрацювання списку використайте лямбда-функцію.

"""

mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
n=int(input("Уведіть окреме число: "))
kv = list(map(lambda x: x-n ,mas))
print(kv)

"""**Задача 3.** 

За умовою попередньої задачі виведіть лише додатні елементи отриманого списку.
"""

mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
n=int(input("Уведіть окреме число: "))
kv = list(map(lambda x: x-n ,mas))
print(*filter(lambda x: x > 0,kv))

"""**Сортування**

Сортування лінійних структур: списків, кортежів, множин, 
словників
"""

sp = sorted([3, 2, 5 ,4, 7, 1])
print(sp)
sp = sorted(sp, reverse=True)
print(sp)
t = ('Zane', 'Bob', 'Janet')
t = sorted(t)
print(t)
s = {'я', 'ти', 'він', 'вона'}
s = sorted(s)
print(s)
d = {1:'a', 2:'b', 3:'c'}
d = sorted(d)
print(d)

"""Сортування словників за ключем та за значенням"""

d = {'mark':25, 'ball':13, 'sun':100, 'cat':88}
print(d.keys())
print(d.values())
print(d.items())

print(sorted(d.items()))

d_sort = sorted(d.items(), key=lambda x: x[1])
print(d_sort)

for k, v in d_sort:
  print(k, ':', v)