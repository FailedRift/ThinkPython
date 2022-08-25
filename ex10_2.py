def cumsum(list):
    cum_list = []
    total = 0
    for i in list:
        total += i
        cum_list.append(total)
    return cum_list

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cumsum(t))
