def sequential_search(list_,n):   # list_ is Python List and n is item we want to search.
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found


numbers = list(range(0,20))
print(sequential_search(numbers, 20))