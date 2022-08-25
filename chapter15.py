class Time:
     """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -=60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.minute += time.second // 60
        time.second = time.second % 60
    if time.minute >= 60:
        time.hour += time.minute // 60
        time.minute = time.minute % 60
        
    #print(time.second, time.minute, time.hour)
    return time
def pure_increment():
    newtime = Time()
    

blank = Time()
blank.hour = 10
blank.minute = 20
blank.second = 40

added = 3600

New = increment(blank, added)
print_time(New)