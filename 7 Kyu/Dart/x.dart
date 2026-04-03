def solution(text, ending):
    x = len(text) - len(ending)
    sliced = text[x:]
    
    return True if sliced == ending else False
