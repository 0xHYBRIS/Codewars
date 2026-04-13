def reverse_words(text):
    reversed = []
    space_index = []
    word_index = []
    words = []
    
    index = 0
    for char in text:
        if char == " ":
            space_index.append(index)
        else:
            words.append(char)
            word_index.append(index)
        index += 1
    
    return word_index
            
