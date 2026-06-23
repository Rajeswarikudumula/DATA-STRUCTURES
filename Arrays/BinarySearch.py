# Program: Binary Search in Python
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Note: Array must be sorted for Binary Search to work

def binary_search(col, key):
    """
    Search for key in sorted array using Binary Search
    Returns index if found, else -1
    """
    li = 0 # lower index
    hi = len(col) - 1 # higher index

    while li <= hi:
        mid = (li + hi) // 2

        if col[mid] == key:
            return mid # Key found
        elif col[mid] < key:
            li = mid + 1 # Search right half
        else:
            hi = mid - 1 # Search left half

    return -1 # Key not found

col = eval(input("Enter the sorted list: "))
key = int(input("Enter the key to search: "))
res=binary_search(col,key)
if res!= -1:
  print(f"Element {key} found at index {res}")
else:
  print(f"Element {key} not found in array")

    
