def count_by(x, n):
    list = []
    
    for i in range(x, (x * n) + 1, x):
        list.append(i)
    
    return list
    
