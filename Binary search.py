def binary_search(arr, target):
    # Initialize the search range boundaries.
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Calculate the middle index.
        mid = (left + right) // 2

        # Check if the middle element is the target.
        if arr[mid] == target:
            return mid  # Found the target, return its index.
        elif arr[mid] < target:
            # If the target is greater, narrow the search to the right half.
            left = mid + 1
        else:
            # If the target is smaller, narrow the search to the left half.
            right = mid - 1

    # If the target is not in the list, return -1 to indicate not found.
    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 7
result = binary_search(my_list, 90)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
