def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = -1

    while j >= -len(word2):
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    
    return True
