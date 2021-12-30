def insertionSort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            print("  ", j, arr, key)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(i,arr, key)

arr = [12,11,13,5,6]
insertionSort(arr)