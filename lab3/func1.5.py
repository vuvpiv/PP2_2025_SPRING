def get_permutations(s):
    if len(s) == 1:
        return [s]  
    permutations = []
    for i in range(len(s)):  
        for perm in get_permutations(s[:i] + s[i+1:]): 
            permutations.append(s[i] + perm)  
    return permutations  

user_input = input("Введите строку: ")
permutations = get_permutations(user_input)
for p in permutations:
    print(p)
