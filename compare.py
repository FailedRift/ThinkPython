def compare(x, y):
    '''Takes 2 integers, x and y, and makes a simple comparison:
    it returns 0 if they are equal.
    returns 1 if x is greater than y
    returns -1 if x is less than y'''
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

