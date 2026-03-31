def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def classify_number(n):
    if n == 0:
        return "zero"
    
    if is_positive(n):  
        signo = "positive"
    else:
        signo = "negative"
    
    if is_even(n):      
        parity = "even"
    else:
        parity = "odd"
    
    return f"{signo} {parity}"



