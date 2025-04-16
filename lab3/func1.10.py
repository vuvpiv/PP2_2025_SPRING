def unique_elements(lst):
    unique_lst = []  
    for item in lst:
        if item not in unique_lst:  
            unique_lst.append(item)  
    return unique_lst
numbers = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in numbers ]
print("Список уникальных элементов:", unique_elements(numbers))