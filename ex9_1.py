to_read = open('words.txt')

for line in to_read:
    if len(line) > 20:
        word_20 = line.strip()
        print(word_20)

