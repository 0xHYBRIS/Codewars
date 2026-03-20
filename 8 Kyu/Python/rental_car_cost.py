def rental_car_cost(d):
    total_cost = d * 40
    if d >= 3 and d < 7:
        total_cost -= 20
    elif d >= 7:
        total_cost -= 50
    
        
    return total_cost
