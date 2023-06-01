from random import *
mas = []
for i in range(3): 
      row = [] 
      for j in range(4): 
           x = randint(-5, 10) 
           row.append(x) 
      mas.append(row)
for i in mas: 
    print(' '.join(list(map(str, i))))
    
row_sum=0
for i in mas:
     row_sum+=sum(i)
print("Сума: " + str(row_sum))

for i in mas:
     print("Мінімальне значення у " +str(mas.index(i)+1)+" рядку:"+ str(min(i)))
     
count=0
for i in mas:
     for j in i:
          if j<0: count+=1
print("Кількість від'ємних значень у двовимірному масиві:"+str(count))


        
