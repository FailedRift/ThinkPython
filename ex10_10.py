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