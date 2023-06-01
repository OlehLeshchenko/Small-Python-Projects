mas = [10, 5, 7, 10, 8, 8, 10, 5, 12]
mas1=[0]*13
for i in mas: mas1[i]=mas.count(i)
mas.clear()
for i in range(len(mas1)):
    for _ in range(mas1[i]):
        mas.append(i)
print(mas)
    
