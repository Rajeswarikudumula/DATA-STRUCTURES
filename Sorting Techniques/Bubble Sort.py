# Program: Bubble Sort in Python
# Time Complexity: O(n^2) worst/avg, O(n) best
# Space Complexity: O(1)
# Note: In-place sorting algorithm

def bubble_sort(arr):
    """
    Sorts array in ascending order using Bubble Sort
    Swaps adjacent elements if they are in wrong order
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False # Optimization: stop if already sorted

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if element found is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is sorted
        if not swapped:
            break

    return arr

arr = list(map(int, input("Enter array elements with spaces: ").split()))

print(f"Original array: {arr}")
sorted_arr = bubble_sort(arr)
print(f"Sorted array: {sorted_arr}")
