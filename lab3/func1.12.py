def histogram(lst):
    for num in lst:
        print('*' * num)  
numbers = input("Введите числа через пробел: ").split()  
numbers = [int(num) for num in numbers]  
histogram(numbers)
