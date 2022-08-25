import bisect

def make_word_list():
    """Reads line from a file and makes a list using the append method.
    
    returns: a list of strings
    """
    word_list = []
    words = open("words.txt")
    for i in words:
        word = i.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list, word):
    """Checks whether a word is in word_list using the bisect method.
    
    word_list: list of strings
    word: string.
    """
    if len(word_list) == 0:
        return False
    
    i = len(word_list)//2
    if word_list[i] == word:
        return True
    
    if word_list[i] > word:
        return in_bisect(word_list[:i], word)
    else:
        return in_bisect(word_list[i:], word)
    
def in_bisect_cheat(word_list, word):
    """Uses the bisection search module"""

    i= bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    
    return word_list[i] == word


word_list = make_word_list()

for word in ['alien', 'altitude', 'bottle', 'cumbersome', 'drink', 'fuck', 'quirk', 'troll', 'zola']:
    print(word, 'in list', in_bisect(word_list, word))

for word in ['alien', 'altitude', 'bottle', 'cumbersome', 'drink', 'fuck', 'quirk', 'troll', 'zola']:
    print(word, 'in list', in_bisect_cheat(word_list, word))