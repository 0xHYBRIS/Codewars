def unique_in_order(sequence):
    unique = []
    
    if len(unique) == 0:
        unique.append(sequence[])
            
    for unique_items in unique:
        for items in sequence:
            if items == unique_items:
                pass
            else:
                unique.append(items)
                
            
    return unique
