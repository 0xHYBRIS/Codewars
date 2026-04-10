def open_or_senior(data):
    
    category = []
    for pairs in data:
        if pairs[0] >= 55 and pairs[1] > 7:
            category.append("Senior")
        else:
            category.append("Open")
            
    
    return category
