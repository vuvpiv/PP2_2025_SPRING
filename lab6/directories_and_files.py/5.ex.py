def writes(list_of_elements):
    with open("test.txt", 'a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        
    
 

writes(["abc", "ABC", 56857, 548, "vhjf"])