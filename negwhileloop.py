def counter(word, letter, start):
    index = start
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)

counter("mississippi", "i", 0)
counter("mississippi", "s", 0)