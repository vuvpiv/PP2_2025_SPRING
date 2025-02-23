import re

def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

with open('row.txt', 'r') as file:
    for line in file:
        if match_pattern(line.strip()) == True:
            print(line.strip())  

