def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        i = 1
        while i < n:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Swap the elements
                swapped = True
            i += 1

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
std_name=["jannat","rizwan","qayum","abhia","hadia","naseem"]
bubble_sort(std_name)
print(std_name)


