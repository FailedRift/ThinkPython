def has_duplicates(list):
    '''Takes a list, checks and returns True if any element repeats,
    or False if it doesn't'''
    sortlist = sorted(list) # Variable that stores the sorted list
    
    # for loop that iterates through the items on sort list
    for i in range(len(sortlist)):
        # to check if we have gotten to the last item in the list
        # if we haven't found any duplicate at this point, nothing is next
        if i == len(sortlist) - 1:
            return False
        # Compares current item with the next item. 
        if sortlist[i] == sortlist[i+1]:
            return True

                     
        
print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 2, 3, 4, 5, 5, 5]))