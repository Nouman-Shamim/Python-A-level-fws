def insertion_sort(arr):
    # Traverse through the entire array.
    for i in range(1, len(arr)):
        # Store the current element to be inserted.
        current_element = arr[i]
        
        # Initialize a pointer to the previous element.
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than current_element
        # one position ahead of their current position.
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the current_element into its correct position.
        arr[j + 1] = current_element

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
