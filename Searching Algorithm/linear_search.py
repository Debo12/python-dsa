def search(array, value):
    for i in range(len(array)):
        if value == array[i]:
            return i
    return -1

array = [10, 50, 30, 45, 60, 79, 86, 34, 50]
value = 50
print(search(array=array, value=value))