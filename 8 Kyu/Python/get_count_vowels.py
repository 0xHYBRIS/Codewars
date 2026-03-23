def get_count(sentence):
    count = 0
    
    for letters in sentence:
        if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":
            count += 1
        else:
            pass
    
    return count
