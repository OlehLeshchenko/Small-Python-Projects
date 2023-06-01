mas = list(map(int, input("Уведіть список чисел через пробіл: ").split())) 
n = len(mas)
k1 = n//2
k2 = n - k1
mas1=[]
mas2=[]
for i in range(k1): mas1.append(mas[i])
for i in range(k1, n, 1): mas2.append(mas[i])
mas1.sort()
mas2.sort()
mas.clear()
while k1>0 and k2>0:
    if mas1[0] <= mas2[0]:
        mas.append(mas1[0])
        k1-=1
        i=0
        while i<k1:
            mas1[i]=mas1[i+1]
            i+=1
    else:
        mas.append(mas2[0])
        k2=k2-1
        i=0
        while i<k2:
            mas2[i]=mas2[i+1]
            i+=1
if k1==0: mas.extend(mas2)
else: mas.extend(mas1)
for i in range(n):
    print(mas[i], end=" ")
