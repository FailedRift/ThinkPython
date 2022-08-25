import time

def make_word_list1():
    word_list = []
    words = open("words.txt")
    for i in words:
        word = i.strip()
        word_list.append(word)
    return word_list


def make_word_list2():
    word_list = []
    words = open("words.txt")
    for i in words:
        word = i.strip()
        word_list = word_list + [word]
    return word_list

start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:20])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:20])
print(elapsed_time, 'seconds')