import math

def mysqrt(a):
    x = a - 1
    while True:
        rt_est = (x + a/x) / 2
        if abs(rt_est - x) < too_close:
            break
        x = rt_est
    return rt_est
too_close = 0.00000000001


def test_square_root(a):
    print("a    mysqrt(a)     math.sqrt(a)     diff")
    print("---  ---------     ------------     ----")
    print("1.0  1.0           1.0              0.0")
    
    for i in range(2,a+1):
        col1 = (float(i))
        col2 = mysqrt(i)
        col3 = math.sqrt(i)
        col4 = col2 - col3
        print(f'{col1}  {col2}     {col3}     {col4}')

test_square_root(9)