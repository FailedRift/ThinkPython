def is_palindrome(word):
    i = 0
    j= len(word)-1

    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j -1
    
    return True

def palindrome_numbers():
   n = 100000
   while True:
    n = n +1
    if n > 999999:
        break
    number = str(n)
    last_four = number[2:]
    if is_palindrome(last_four):
        print(n)
        number = str(n+1)
        last_five = number[1:]
        if is_palindrome(last_five):
            print(n+1)
            number = str(n+2)
            middle_four = number[1:4]
            if is_palindrome(middle_four):
                print(n+2)
                number = str(n+3)
                if is_palindrome(number):
                    print(n+3)
                    return n
                else:
                    continue
            else: 
                continue
        else: 
            continue
    else:
        continue

                    
palindrome_numbers()