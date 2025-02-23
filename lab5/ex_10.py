import re

def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()


camel_case_string = input()
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)