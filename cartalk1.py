def two_consecutive_letters(word, n):
    while n < len(word)-1:
        if word[n] == word[n+1]:
            return True
        else:
            return False


def triple_consecutive(word):
    i = 0
    while i < len(word)-1:
        if two_consecutive_letters(word, i):
            i = i + 2
            if two_consecutive_letters(word, i):
                i= i + 2
                if two_consecutive_letters(word, i):
                    return True
        else:
            i = i + 1 
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if triple_consecutive(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
