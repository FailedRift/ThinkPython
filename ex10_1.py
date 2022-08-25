def nested_sum(list):
    sum = 0 
    for i in range(len(list)):
        total = 0
        for x in list[i]:
            total += x
        sum += total
    return sum
            

t = [[1, 2], [3], [4, 5, 6]]
m = [ [2, 3, 4, 5, 6,], [4, 1, 9, 9], [8, 7, 7, 7]] 

print(nested_sum(t))
print(nested_sum(m))