def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in list(str1):
        if i not in list(str2):
            return False
        else:
            return True

