def bubbleSort(arr):
    n = length(arr)
    swapped = True

    while swapped:
        swapped = False

        for i from 1 to n-1:
            if arr[i-1] > arr[i]:
                # Swap the elements
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

# Example usage:
myArray = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(myArray)
print("Sorted array is:", myArray)
