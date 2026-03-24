def get_sum(a,b):
    sum = 0
    
    head = a if a > b else b
    tail = a if a < b else b

    for nums in range(tail, head + 1):
        sum += nums
    
    return sum
