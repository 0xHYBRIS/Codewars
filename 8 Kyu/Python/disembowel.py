def disemvowel(string_):
    new_string = []
    for char in string_:
        if char.lower() == "a" or char.lower() == "e" or  char.lower() == "i" or  char.lower() == "o" or  char.lower() == "u":
            new_string.append("")
        else:
            new_string.append(char)
        
    return "".join(new_string)
