
def bubblesort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array

print(bubblesort([7,3,5,6]))

