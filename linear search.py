def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # If the target is not found, return -1

# Example usage:
my_list = [10, 25, 3, 45, 20, 8]
target_element = 45

result = linear_search(my_list, target_element)

if result != -1:
    print("Element", target_element," found at index ",result)
else:
    print("Element", target_element," not found in the list.")
