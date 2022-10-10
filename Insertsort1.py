def insertsort(array):
    for blackptr in range(1, len(array)):
        for blueptr in range(0, blackptr):
            if array[blackptr] < array[blueptr]:
                temp = array[blackptr]
                for i in range(blackptr-1, blueptr-1, -1):
                    array[i+1] = array[i]
                array[blueptr] = temp
                break
            
