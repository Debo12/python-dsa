import math

def search(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((end+start)/2)

    while(array[middle]!=value and start<=end):
        if array[middle]>value:
            end = middle-1
        else:
            start = middle+1
        middle = math.floor((end+start)/2)

    if array[middle] == value:
        return middle
    return -1

array = [3, 8, 15, 22, 27, 34, 41, 56, 63, 78]
value = 41
print(search(array=array, value=value))