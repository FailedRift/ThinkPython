def histogram(s):
    d = dict()
    for c in s:
        b = d.get(c , 0)
        b += 1
        d[c] = b
    return d

print(histogram('mississippi'))
