def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

snake_case_string = input("Enter a snake case string: ")
camel_case_string = snake_to_camel(snake_case_string)

print(f'Snake case: {snake_case_string}')
print(f'Camel case: {camel_case_string}')
