# Program: Ternary Search in Python
# Time Complexity: O(log3 n)
# Space Complexity: O(1)
# Note: Array must be SORTED

def ternary_search(arr, key):
    """
    Search for key in sorted array using Ternary Search
    Returns index if found, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            right = mid1 - 1 # Search in 1st part
        elif key > arr[mid2]:
            left = mid2 + 1 # Search in 3rd part
        else:
            left = mid1 + 1 # Search in middle part
            right = mid2 - 1

    return -1

arr = list(map(int, input("Enter sorted array with spaces: ").split()))
key = int(input("Enter key to search: "))

result = ternary_search(arr, key)

if result!= -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in array")
