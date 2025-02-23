import re

def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)


print(insert_spaces(input()))  
