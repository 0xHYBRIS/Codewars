def reverse_words(text):
    # I'm screwed if someone read this bs answer
    reversed = []
    space_index = []
    word_index = []
    words = []
    
    index = 0
    for char in text:
        if char == " ":
            pass
        else:
            words.append(char)
            word_index.append(index)
        index += 1
    
    for chars in range(len(text) - 1):
        if chars not in word_index
    return word_index
            
