def sed(pattern, replace, file1, file2):
    f1 = open(file1, encoding="utf-8")
    f2 = open(file2, 'w')
    res = f1.read()
