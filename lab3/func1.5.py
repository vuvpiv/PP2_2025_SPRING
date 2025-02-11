def print_permutations(s):
    if len(s) == 1:
        print(s)
    else:
        for i in range(len(s)):
            for perm in print_permutations(s[:i] + s[i+1:]):
                print(s[i] + perm)
user_input = input("Введите строку: ")
print_permutations(user_input)