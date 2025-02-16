n = int(input("Введите число: "))  
countdown = (x for x in range(n, -1, -1)) 
for num in countdown:
    print(num)