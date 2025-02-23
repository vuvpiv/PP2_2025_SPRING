import re

def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    match = pattern.findall(input_string)

    if match:
        print(f'Sequences found: {match}')
    else:
        print('No sequences found.')

input_string = input()
find_sequences(input_string)
