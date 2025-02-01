def reverse_words(sentence):
    words = sentence.split()  
    words.reverse()  
    return " ".join(words) 
user_input = input("Введите строку: ")
print(reverse_words(user_input))