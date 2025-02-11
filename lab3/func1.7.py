def check(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3: 
            return True
    return False  
user_input = input("Введите числа через пробел: ")  
numbers = [int(x) for x in user_input.split()]  
print(check(numbers))  
