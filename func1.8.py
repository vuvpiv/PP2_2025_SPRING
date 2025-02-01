def spy_game(nums):
    sequence = [0, 0, 7]
    for num in nums:
        if num == sequence[0]:
            sequence.pop(0)  
        if len(sequence) == 0:  
            return True
    return False  
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
