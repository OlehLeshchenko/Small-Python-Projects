mas = list(map(int, input("Уведіть список чисел через пробіл: ").split())) 
for i in range(1, len(mas)):
    k = mas[i]
    j = i - 1
    while j >= 0 and mas[j] > k:
        mas[j + 1] = mas[j]
        j -= 1
    mas[j + 1] = k  
print(mas)  
