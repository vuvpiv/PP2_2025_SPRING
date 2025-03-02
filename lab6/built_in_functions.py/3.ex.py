def polindrom(sentence,reverse_sentence):
    for i in sentence:
        for j in reverse_sentence:
            if i!=j:
                return False
                break
            return True
        
    

sentence=str(input("enter sentence:"))
sentence_reverse=''.join(reversed(sentence))
print(polindrom(sentence,sentence_reverse))