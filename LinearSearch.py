def linearsearch(array,val):
    i=0
    isfound = False
    ub = len(array)-1
    while isfound == False and i<=ub:
        if array[i] == val:
            isfound = True
            print(i)
        else:
            i = i+1
    if isfound == False:
        print(-1)
