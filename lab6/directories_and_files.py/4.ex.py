import os
import string

with open("test.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()