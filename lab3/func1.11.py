def is_palindrome(s):
    s = s.lower()  
    return s ==  "".join(reversed(s))


word = input("Введите слово или фразу: ")
if is_palindrome(word):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
