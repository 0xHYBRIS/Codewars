def printer_error(s):
    invalid_chars = "nopqrstuvwxyz"
    err_count = 0
    
    for char in s:
        if char in invalid_chars:
            err_count += 1
        else:
            pass
    
    return f"{err_count}/{len(s)}"
#Easy
