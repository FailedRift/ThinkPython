to_read = open('words.txt')

def no_e(word):
    if 'e' in word:
        return True


total = 0
total_ne = 0
for line in to_read:
    total = total + 1
    word_20 = line.strip()
    if  not no_e(word_20):
       total_ne = total_ne + 1

print(f"percentage of words in the list that do not have e is:{(total_ne/total) * 100}%") 
