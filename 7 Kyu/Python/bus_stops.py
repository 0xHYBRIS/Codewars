def number(bus_stops):
    people_in = people_out = 0

    for people in bus_stops:
        people_in += people[0]
        people_out += people[1]
            
    return people_in - people_out
