def reverse_words(text):
    reversed = []
    space_index = []
    words = []
    
    index = 0
    for char in text:
        if char == " ":
            space_index.append(index)
        else:
            words.append("")
            
