# Program: Linear Search in Python
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    """
    Search for target in array using Linear Search
    Returns index if found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Driver code to test
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = int(input("Enter element to search: "))

    result = linear_search(arr, target)

    if result!= -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in array")
