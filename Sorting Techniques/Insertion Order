
# Program: Insertion Sort in Python
# Time Complexity: O(n^2) worst/avg, O(n) best
# Space Complexity: O(1)
# Note: In-place, stable. Used in Timsort for small arrays

def insertion_sort(arr):
    """
    Sorts array in ascending order using Insertion Sort
    Builds sorted array one item at a time, like sorting cards
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i] # Element to be inserted
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key # Insert key at correct position

    return arr
    
arr = list(map(int, input("Enter array elements with spaces: ").split()))

print(f"Original array: {arr}")
sorted_arr = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")
