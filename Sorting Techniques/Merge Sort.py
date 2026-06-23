# Program: Merge Sort in Python
# Time Complexity: O(n log n) for all cases
# Space Complexity: O(n) for temporary arrays
# Strategy: Divide and Conquer, stable sort

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays arr[left..mid] and arr[mid+1..right]
    """
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left # Initial index of merged subarray

    # Merge temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """
    Main function that sorts arr[left..right] using merge()
    """
    if left < right:
        mid = left + (right - left) // 2 # Avoid overflow

        merge_sort(arr, left, mid) # Sort first half
        merge_sort(arr, mid + 1, right) # Sort second half
        merge(arr, left, mid, right) # Merge sorted halves

arr = list(map(int, input("Enter array elements with spaces: ").split()))

print(f"Original array: {arr}")
merge_sort(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
