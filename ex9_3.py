def avoids(word, forbids):
    for i in forbids:
        if i in word:
            return
        else:
            print(word)
            return True


to_read = open('words.txt')
forbid = input("Enter forbidden letters:")

for line in to_read:
    word_20 = line.strip()
    avoids(word_20, forbid)


