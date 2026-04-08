def find_it(seq):
    count = 0
    for num in seq:
        
        for each in seq:
            if num == each:
                count += 1
        
        if count % 2 != 0:
            return num
