def insertsort(array):
    for currentnode in range(1, len(array)):
        temp = array[currentnode]
        ptr = currentnode-1
        while array[ptr] > temp and ptr > -1:
            array[ptr+1] = array[ptr]
            ptr = ptr-1
        array[ptr+1] = temp
