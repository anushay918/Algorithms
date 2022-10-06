def recbinsearch(val, array, lb, ub):
    mid = (lb+ub)//2
    if lb>ub:
        print(-1)
    elif array[mid] == val:
        print(mid)
    elif array[mid] < val:
        recbinsearch(val, array, mid+1, ub)
    else:
        recbinsearch(val, array, lb, mid-1)
