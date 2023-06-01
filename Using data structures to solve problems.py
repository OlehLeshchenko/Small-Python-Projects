#1
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
mas1= set(mas)
for i in mas:
    if i in mas1:
        print(i, end=" ")
        mas1.remove(i) 
print(" ")
#10
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split())) 
key = sorted(list(set(mas)), reverse=True)
th=[]
for i in key:
     th.append(mas.count(i))
print(key[th.index(max(th))])
#2
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
print(sorted(list(set(mas))))
#3
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
mas1= set(mas)
result=[]
for i in mas1:
    if mas.count(i)==1: result.append(i)
for i in mas:
    if i in result:
        print(i, end=" ")
        result.remove(i) 
print(" ")
#4
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
result=[]
for i in set(mas):
    if mas.count(i)==1: result.append(i)
print(sorted(result))
#5
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
result=[]
for i in set(mas):
    if mas.count(i)>1: result.append(i)
print(result)
#6
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
print(len(set(mas)))
#7
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
result=[]
for i in set(mas):
    if mas.count(i)>1: result.append(i)
print(len(result))
#8
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
result=[]
for i in set(mas):
    if mas.count(i)==1: result.append(i)
print(len(result))
#9
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split())) 
key = sorted(list(set(mas)))
th=[]
for i in key:
     th.append(mas.count(i))
print(key[th.index(max(th))])
#13
mas = list(map(int, input("Уведіть список чисел через пробіл: ").split()))
avg=sum(mas)/len(mas)
print(avg)
for i in mas:
    if i>avg: print(i, end=" ")
