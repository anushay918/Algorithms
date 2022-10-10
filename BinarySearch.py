def binarysearch(array, val):
    found = False
    ub = len(array)-1
    lb = 0
    while found == False and lb <=ub:
        mid = (ub+lb)//2
        if array[mid] == val:
            print(mid)
            found = True
        elif array[mid] < val:
            lb = mid+1
        else:
            ub = mid-1
    if found == False:
        print('not found')
