class outofchai(Exception):
    pass

def check(size):
    if size> 10:
        raise outofchai("no chai available")

    
check(12)
        
    