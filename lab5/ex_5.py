import re

def match_pattern(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.fullmatch(input_string)

    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

input_string = input()
match_pattern(input_string)
