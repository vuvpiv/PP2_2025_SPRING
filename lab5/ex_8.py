import re

def split_at_uppercase(input_string):
    return re.findall(r'[A-Z][a-z]*', input_string)

print(split_at_uppercase(input()))
