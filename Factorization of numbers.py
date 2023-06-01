n=int(input("Введіть число: "))
n1=n
n2=n
n3=n
d=2
i=0
while n>1:
    if n%d==0:
        print(d)
        n=n//d
    else:
        d+=1
    i+=1
print("Кількість операцій: ",i)

d=3
i=0
while n1>1:
    if n1%2==0:
        print(2)
        n1=n1//2
    elif n1%d==0:
        print(d)
        n1=n1//d
    else: d+=2
    i+=1
print("Кількість операцій: ",i)

d=3
i=0
while n2%2==0:
    print(2)
    n2=n2//2
    i+=1
while n2>1:
    if n2%d==0:
        print(d)
        n2=n2//d
    else: d+=2
    i+=1
print("Кількість операцій: ",i)

i=0
mas=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for k in mas:
    while n3%k==0:
        n3=n3//k
        print(k)
        i+=1
print("Кількість операцій: ",i)

def prime(x):
    if x in [0, 1]:
        return False
    if x == 2:
        return True
    for n in range(3, int(x ** 0.5 + 1)):
        if x % n == 0:
            return False
    return True
for o in range(3000000):
    if prime(o+1)==True:
        print(o+1)
    

