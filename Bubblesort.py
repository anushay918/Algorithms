def bubblesort(array):
    i = -1
    temp = -1
    swapped = True
    Boundary = len(array)-1
    while swapped = True:
        swapped = False
        for i in range(0, Boundary):
            if arrayy[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swapped = True
        Boundary = Boundary-1
