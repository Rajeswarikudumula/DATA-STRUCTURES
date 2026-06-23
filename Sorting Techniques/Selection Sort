# Program: Selection Sort in Python
# Time Complexity: O(n^2) for all cases
# Space Complexity: O(1)
# Note: In-place, but NOT stable

def selection_sort(arr):
    """
    Sorts array in ascending order using Selection Sort
    Finds minimum element and puts it at beginning
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        min_idx = i # Find minimum element in remaining array

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = list(map(int, input("Enter array elements with spaces: ").split()))
print(f"Original array: {arr}")
sorted_arr = selection_sort(arr)
print(f"Sorted array: {sorted_arr}")
