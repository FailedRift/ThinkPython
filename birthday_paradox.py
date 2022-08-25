import random
from ex10_7 import has_duplicates

def birthday_prob(n):
    count = 0
    for i in range(n):
        birthdays = []
        for i in range(22):
            birthdays.append(random.randint(1,365))
        if has_duplicates(birthdays):
            count += 1
    return count / n


print(birthday_prob(10000))