def century(year):
    if year < 100:
        return 1
    elif year >= 100 and year < 1000:
        if (year - (year % 100)) == year:
            return year // 100
        else:
            return (year // 100) + 1
    else:
        if (year - (year % 100)) == year:
            return year // 100
        else:
            return (year // 100) + 1
    
