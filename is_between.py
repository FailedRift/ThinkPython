def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


print(is_between(5, 7, 9))
print(is_between(10, 8, 15))